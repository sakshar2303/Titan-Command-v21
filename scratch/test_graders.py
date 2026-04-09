from backend.my_env import EmergencyEnv, grade_budget, grade_integrity, grade_lives_saved

def test_graders():
    env = EmergencyEnv()
    
    print(f"Initial Budget: {env.budget}")
    print(f"Grade Budget: {grade_budget(env)}")
    
    print(f"Initial Integrity: {env.sector_integrity}")
    print(f"Grade Integrity: {grade_integrity(env)}")
    
    print(f"Initial Lives Saved: {env.lives_saved}")
    print(f"Grade Lives Saved: {grade_lives_saved(env)}")
    
    # Test with dict
    obs = env._get_observation()
    print("Testing with observation dict:")
    print(f"Grade Budget: {grade_budget(obs)}")
    print(f"Grade Integrity: {grade_integrity(obs)}")
    print(f"Grade Lives Saved: {grade_lives_saved(obs)}")

if __name__ == "__main__":
    test_graders()
