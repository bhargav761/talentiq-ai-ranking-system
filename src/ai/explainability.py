import pandas as pd

df = pd.read_csv(
    "data/outputs/top_candidates.csv"
)

candidate = df.iloc[0]

print(
    f"Candidate: {candidate['candidate_id']}"
)

print(
    f"Final Score: {candidate['final_score']:.2f}"
)

print("\nExplanation")

print(
    "- Strong semantic match with JD"
)

print(
    "- High trust score"
)

print(
    "- Good recruiter engagement"
)

print(
    "- Relevant experience"
)