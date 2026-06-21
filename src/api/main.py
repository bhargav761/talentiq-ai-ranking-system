from fastapi import FastAPI
import pandas as pd

app = FastAPI(
    title="TalentIQ API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "TalentIQ AI Candidate Ranking System"
    }

@app.get("/top-candidates")
def get_top_candidates():

    df = pd.read_csv(
        "data/outputs/top_candidates.csv"
    )

    result = (
        df.head(10)
        .to_dict(
            orient="records"
        )
    )

    return result