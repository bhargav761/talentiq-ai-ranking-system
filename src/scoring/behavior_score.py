import pandas as pd

df = pd.read_csv(
    "data/processed/candidates_trust.csv"
)

def calculate_behavior_score(row):

    score = 0

    score += (
        row["github_activity_score"] * 0.40
    )

    score += (
        row["saved_by_recruiters_30d"] * 0.30
    )

    score += (
        row["search_appearance_30d"] * 0.20
    )

    return round(score, 2)

df["behavior_score"] = df.apply(
    calculate_behavior_score,
    axis=1
)

print(
    df[
        [
            "candidate_id",
            "behavior_score"
        ]
    ].head()
)

df.to_csv(
    "data/processed/candidates_behavior.csv",
    index=False
)

print("\nBehavior Score Created")