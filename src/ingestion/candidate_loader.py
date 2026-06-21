import pandas as pd
import json

df = pd.read_json(
    "data/raw/candidates.jsonl",
    lines=True
)

print("Dataset Shape:", df.shape)

print("\nProfile Keys:")
print(df.iloc[0]["profile"].keys())

print("\nRedrob Signal Keys:")
print(df.iloc[0]["redrob_signals"].keys())