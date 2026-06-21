import pandas as pd

df = pd.read_csv(
    "data/processed/candidates_flat.csv"
)

def calculate_trust_score(row):

    score = 0

    score += (
        row["profile_completeness_score"] * 0.30
    )

    score += (
        row["recruiter_response_rate"] * 0.25
    )

    score += (
        row["interview_completion_rate"] * 0.25
    )

    score += (
        row["offer_acceptance_rate"] * 0.20
    )

    return round(score, 2)

df["trust_score"] = df.apply(
    calculate_trust_score,
    axis=1
)

print(
    df[
        ["candidate_id", "trust_score"]
    ].head()
)

df.to_csv(
    "data/processed/candidates_trust.csv",
    index=False
)

print("\nTrust Score Created")