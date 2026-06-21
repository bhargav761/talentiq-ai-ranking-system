import pandas as pd

from sentence_transformers import SentenceTransformer, util

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading dataset...")

df = pd.read_json(
    "data/raw/candidates.jsonl",
    lines=True
)

with open(
    "data/raw/job_description.txt",
    "r",
    encoding="utf-8"
) as f:
    job_description = f.read()

job_embedding = model.encode(
    job_description,
    convert_to_tensor=True
)

scores = []

print("Processing candidates...")

for _, row in df.head(100).iterrows():

    profile = row["profile"]

    candidate_text = (
        str(profile.get("headline", ""))
        + " "
        + str(profile.get("summary", ""))
    )

    candidate_embedding = model.encode(
        candidate_text,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        job_embedding,
        candidate_embedding
    )

    scores.append({
        "candidate_id": row["candidate_id"],
        "semantic_score": float(similarity)
    })

result = pd.DataFrame(scores)

result = result.sort_values(
    "semantic_score",
    ascending=False
)

result.to_csv(
    "data/processed/candidates_semantic.csv",
    index=False
)

print(result.head(10))

print("\nSemantic Scores Saved")