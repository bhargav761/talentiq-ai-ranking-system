import pandas as pd

# Load data
df = pd.read_csv(
    "data/processed/candidates_experience.csv"
)

semantic = pd.read_csv(
    "data/processed/candidates_semantic.csv"
)

# Merge semantic score
df = df.merge(
    semantic,
    on="candidate_id",
    how="left"
)

# Fill missing values
df["semantic_score"] = (
    df["semantic_score"]
    .fillna(0)
)

# Normalize scores
df["trust_norm"] = (
    df["trust_score"]
    / df["trust_score"].max()
)

df["behavior_norm"] = (
    df["behavior_score"]
    / df["behavior_score"].max()
)

df["experience_norm"] = (
    df["experience_score"]
    / 100
)

df["semantic_norm"] = (
    df["semantic_score"]
    / df["semantic_score"].max()
)

# Final ranking formula
df["final_score"] = (
    0.35 * df["semantic_norm"] +
    0.25 * df["trust_norm"] +
    0.20 * df["behavior_norm"] +
    0.20 * df["experience_norm"]
)

# Sort candidates
ranked = df.sort_values(
    "final_score",
    ascending=False
)

# Save output
ranked.to_csv(
    "data/outputs/top_candidates.csv",
    index=False
)

print("\nTop 20 Candidates\n")

print(
    ranked[
        [
            "candidate_id",
            "final_score",
            "semantic_score",
            "trust_score",
            "behavior_score",
            "experience_score"
        ]
    ].head(20)
)

print("\nFinal Ranking Generated")