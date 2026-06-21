import pandas as pd

df = pd.read_csv(
    "data/outputs/top_candidates.csv"
)

candidate = df.iloc[0]

print("\n===== RECRUITER COPILOT =====\n")

print(
    f"Candidate ID: {candidate['candidate_id']}"
)

print(
    f"Final Score: {candidate['final_score']:.2f}"
)

print("\nWhy Should You Hire This Candidate?\n")

if candidate["semantic_score"] > 0.60:
    print("✓ Strong match with job requirements")

if candidate["trust_score"] > 20:
    print("✓ High trust and profile quality")

if candidate["behavior_score"] > 20:
    print("✓ Active and engaged candidate")

if candidate["experience_score"] > 50:
    print("✓ Relevant industry experience")

print("\nRecommendation:")
print(
    "Proceed to technical interview."
)