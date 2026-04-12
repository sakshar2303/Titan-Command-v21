"""tasks/graders.py - Titan Command v21 - OpenEnv Graders

These graders are referenced by openenv.yaml and called by the evaluator.
Each grader MUST return a float strictly in (0, 1) — never 0.0 or 1.0.

Grader signatures accept (*args, **kwargs) so they work regardless of
whether the evaluator passes (env,), (env, history), or other combinations.
"""
import math

# ---------------------------------------------------------------------------
# Internal helpers — zero external dependencies
# ---------------------------------------------------------------------------

def _clamp(score: float) -> float:
    """Force score into (0.05, 0.95) — strict open interval with safety buffer."""
    try:
        s = float(score)
        if math.isnan(s) or math.isinf(s):
            return 0.50
        # Narrowed range to ensure we never hit 0.0 or 1.0 even with rounding
        return max(0.05, min(0.95, s))
    except Exception:
        return 0.50

def _extract_metric(env, key, default):
    """Safely extracts a numeric value from an environment or dict."""
    if env is None:
        return float(default)
    
    try:
        # Handle Case 1: Standard attribute (env.budget)
        if hasattr(env, key):
            val = getattr(env, key)
            if val is not None:
                return float(val)

        # Handle Case 2: Dictionary (e.g. observation or info dict)
        if isinstance(env, dict):
            if key in env and env[key] is not None:
                return float(env[key])
            # Fallback for common aliases
            aliases = {
                "budget": ["remaining_budget", "total_budget"],
                "sector_integrity": ["integrity", "health"],
                "lives_saved": ["saved", "score"]
            }
            for alt_key in aliases.get(key, []):
                if alt_key in env and env[alt_key] is not None:
                    return float(env[alt_key])
        
        # Handle Case 3: List (History/Trajectory)
        if isinstance(env, list) and len(env) > 0:
            last_step = env[-1]
            return _extract_metric(last_step, key, default)
                    
    except (ValueError, TypeError):
        pass
    
    return float(default)

def _safe_sigmoid(x: float) -> float:
    """Logistic sigmoid with safe range for float precision."""
    try:
        if math.isnan(x) or math.isinf(x):
            return 0.5
        # Cap x to avoid overflow in exp
        x = max(-50.0, min(50.0, x))
        return 1.0 / (1.0 + math.exp(-x))
    except Exception:
        return 0.5

# ---------------------------------------------------------------------------
# Public graders — referenced from openenv.yaml
# ---------------------------------------------------------------------------

def grade_budget(*args, **kwargs) -> float:
    """Grades performance based on remaining budget. (Easy Task)"""
    env = args[0] if args else kwargs.get("env") or kwargs.get("environment")
    val = _extract_metric(env, "budget", 120000.0)
    # Range centered at 60k. 120k -> ~0.95, 0 -> ~0.05
    x = (val / 120000.0) * 6.0 - 3.0
    return _clamp(_safe_sigmoid(x))

def grade_integrity(*args, **kwargs) -> float:
    """Grades performance based on sector integrity. (Fallback)"""
    env = args[0] if args else kwargs.get("env") or kwargs.get("environment")
    val = _extract_metric(env, "sector_integrity", 100.0)
    # Range centered at 50. 100 -> ~0.95, 0 -> ~0.05
    x = (val / 100.0) * 6.0 - 3.0
    return _clamp(_safe_sigmoid(x))

def grade_lives_saved(*args, **kwargs) -> float:
    """Grades performance based on lives saved. (Medium Task)"""
    env = args[0] if args else kwargs.get("env") or kwargs.get("environment")
    val = _extract_metric(env, "lives_saved", 0.0)
    # Target 50 lives for 0.5 score, 100+ for ~0.8+
    x = (val / 50.0) * 4.0 - 2.0
    return _clamp(_safe_sigmoid(x))

def grade_efficiency(*args, **kwargs) -> float:
    """Grades efficiency (lives saved vs budget spent). (Hard Task)"""
    env = args[0] if args else kwargs.get("env") or kwargs.get("environment")
    lives = _extract_metric(env, "lives_saved", 0.0)
    budget = _extract_metric(env, "budget", 120000.0)
    budget_used = max(0, 120000.0 - budget)
    
    if budget_used < 1000:
        return 0.50 # Neutral score for no activity
        
    efficiency = lives / (budget_used / 10000.0)
    # Target 5 lives per 10k budget for 0.5 score
    x = (efficiency / 5.0) * 4.0 - 2.0
    return _clamp(_safe_sigmoid(x))
