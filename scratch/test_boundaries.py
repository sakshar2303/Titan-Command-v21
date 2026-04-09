from backend.my_env import EmergencyEnv, grade_budget, grade_integrity, grade_lives_saved

def test_boundaries():
    print("Testing Boundary Conditions:")
    
    # 1. Zero/Minimal values
    obs_zero = {"budget": 0, "integrity": 0, "lives_saved": 0}
    print(f"Zeros -> Budget: {grade_budget(obs_zero)}, Integrity: {grade_integrity(obs_zero)}, Lives: {grade_lives_saved(obs_zero)}")
    
    # 2. Maximum/Extreme values
    obs_max = {"budget": 999999, "integrity": 100, "lives_saved": 999999}
    print(f"Max -> Budget: {grade_budget(obs_max)}, Integrity: {grade_integrity(obs_max)}, Lives: {grade_lives_saved(obs_max)}")
    
    # 3. None/Missing values (should use defaults)
    obs_none = {}
    print(f"None -> Budget: {grade_budget(obs_none)}, Integrity: {grade_integrity(obs_none)}, Lives: {grade_lives_saved(obs_none)}")

if __name__ == "__main__":
    test_boundaries()
