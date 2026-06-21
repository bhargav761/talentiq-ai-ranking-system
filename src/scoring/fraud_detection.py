import pandas as pd

df = pd.read_json(
    "data/raw/candidates.jsonl",
    lines=True
)

results = []

for _, row in df.head(100).iterrows():

    profile = row["profile"]

    years = profile.get(
        "years_of_experience",
        0
    )

    skills = row.get(
        "skills",
        []
    )

    skill_count = len(skills)

    risk_flags = []

    if years < 2 and skill_count > 20:
        risk_flags.append(
            "Possible Skill Inflation"
        )

    if years < 1 and skill_count > 30:
        risk_flags.append(
            "High Skill Inflation Risk"
        )

    results.append({
        "candidate_id":
            row["candidate_id"],

        "years_of_experience":
            years,

        "skill_count":
            skill_count,

        "risk":
            ", ".join(risk_flags)
            if risk_flags
            else "Low Risk"
    })

fraud_df = pd.DataFrame(results)

print(
    fraud_df.head(20)
)

fraud_df.to_csv(
    "data/outputs/fraud_detection.csv",
    index=False
)

print(
    "\nFraud Detection Report Generated"
)