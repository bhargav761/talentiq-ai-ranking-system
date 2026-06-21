import pandas as pd

df = pd.read_csv(
    "data/processed/candidates_behavior.csv"
)

def calculate_experience_score(row):

    years = row["years_of_experience"]

    if years >= 10:
        return 100

    return years * 10

df["experience_score"] = df.apply(
    calculate_experience_score,
    axis=1
)

print(
    df[
        [
            "candidate_id",
            "experience_score"
        ]
    ].head()
)

df.to_csv(
    "data/processed/candidates_experience.csv",
    index=False
)

print("\nExperience Score Created")