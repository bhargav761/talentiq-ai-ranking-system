import pandas as pd

df = pd.read_json(
    "data/raw/candidates.jsonl",
    lines=True
)

flattened = []

for _, row in df.iterrows():

    profile = row["profile"]
    signals = row["redrob_signals"]

    flattened.append({
        "candidate_id": row["candidate_id"],
        "headline": profile.get("headline"),
        "years_of_experience": profile.get("years_of_experience"),
        "current_title": profile.get("current_title"),
        "current_company": profile.get("current_company"),

        "profile_completeness_score":
            signals.get("profile_completeness_score"),

        "github_activity_score":
            signals.get("github_activity_score"),

        "recruiter_response_rate":
            signals.get("recruiter_response_rate"),

        "search_appearance_30d":
            signals.get("search_appearance_30d"),

        "saved_by_recruiters_30d":
            signals.get("saved_by_recruiters_30d"),

        "interview_completion_rate":
            signals.get("interview_completion_rate"),

        "offer_acceptance_rate":
            signals.get("offer_acceptance_rate")
    })

flat_df = pd.DataFrame(flattened)

print(flat_df.head())

print("\nShape:")
print(flat_df.shape)

flat_df.to_csv(
    "data/processed/candidates_flat.csv",
    index=False
)