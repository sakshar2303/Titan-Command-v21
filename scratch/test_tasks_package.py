from tasks.graders import grade_budget, grade_integrity, grade_lives_saved

def test_tasks_package():
    print("Testing Graders in tasks/package:")
    
    # Test with dummy observation
    obs = {"budget": 120000, "integrity": 100, "lives_saved": 0}
    
    b_score = grade_budget(obs)
    i_score = grade_integrity(obs)
    l_score = grade_lives_saved(obs)
    
    print(f"Budget Score: {b_score}")
    print(f"Integrity Score: {i_score}")
    print(f"Lives Score: {l_score}")
    
    # Check range (strictly between 0 and 1)
    for name, score in [("Budget", b_score), ("Integrity", i_score), ("Lives", l_score)]:
        assert 0.0 < score < 1.0, f"{name} score {score} out of range!"
        assert score != 0.0 and score != 1.0, f"{name} score {score} is exactly boundary!"
    
    print("✅ All scores within (0, 1) range.")

if __name__ == "__main__":
    test_tasks_package()
