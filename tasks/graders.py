import math

def _extract_metric(env, key, default=0.0):
    """
    Extracts a numeric metric from an environment object, observation dict, or list of steps.
    """
    try:
        if env is None:
            return float(default)
        
        # 1. Try attribute access (Environment object)
        if hasattr(env, key):
            val = getattr(env, key)
            if val is not None:
                return float(val)
        
        # 2. Try dictionary access (Observation dict)
        if isinstance(env, dict):
            if key in env:
                return float(env[key])
            if key == "sector_integrity" and "integrity" in env:
                return float(env["integrity"])
            if key == "integrity" and "sector_integrity" in env:
                return float(env["sector_integrity"])
        
        # 3. Try list access (History or Trajectory)
        if isinstance(env, list) and len(env) > 0:
            last_step = env[-1]
            if isinstance(last_step, dict) and key in last_step:
                return float(last_step[key])
                
    except (ValueError, TypeError, KeyError):
        pass
    
    return float(default)

def _safe_sigmoid(x: float) -> float:
    try:
        if math.isnan(x) or math.isinf(x):
            return 0.5
        x = max(-500.0, min(500.0, x))
        return 1.0 / (1.0 + math.exp(-x))
    except Exception:
        return 0.5

def grade_budget(env) -> float:
    """Grades performance based on remaining budget. Range: [0.01, 0.99]"""
    val = _extract_metric(env, "budget", 120000.0)
    x = (val / 120000.0) * 6.0 - 3.0
    score = _safe_sigmoid(x)
    return float(max(0.01, min(0.99, score)))

def grade_integrity(env) -> float:
    """Grades performance based on sector integrity. Range: [0.01, 0.99]"""
    val = _extract_metric(env, "sector_integrity", 100.0)
    x = (val / 100.0) * 6.0 - 3.0
    score = _safe_sigmoid(x)
    return float(max(0.01, min(0.99, score)))

def grade_lives_saved(env) -> float:
    """Grades performance based on lives saved. Range: [0.01, 0.99]"""
    val = _extract_metric(env, "lives_saved", 0.0)
    x = (val / 5000.0) * 6.0 - 3.0
    score = _safe_sigmoid(x)
    return float(max(0.01, min(0.99, score)))
