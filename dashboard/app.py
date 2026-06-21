import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TalentIQ",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 TalentIQ AI Candidate Ranking System")

df = pd.read_csv("data/outputs/top_candidates.csv")

tab1, tab2, tab3, tab4 = st.tabs([
    "🏆 Top Candidates",
    "📊 Skill Gap Analysis",
    "🤖 Recruiter Copilot",
    "🚨 Fraud Detection"
])

with tab1:
    st.header("Top Ranked Candidates")
    st.dataframe(df.head(20), use_container_width=True)

    top_candidate = df.iloc[0]

    st.success(
        f"Top Candidate: {top_candidate['candidate_id']}"
    )

    st.metric(
        "Final Score",
        round(top_candidate["final_score"], 2)
    )

with tab2:
    st.header("Skill Gap Analysis")

    job_skills = [
        "AWS",
        "Docker",
        "Terraform",
        "Kubernetes"
    ]

    candidate_skills = [
        "AWS",
        "Docker",
        "Linux"
    ]

    matched_skills = list(
        set(job_skills) &
        set(candidate_skills)
    )

    missing_skills = list(
        set(job_skills) -
        set(candidate_skills)
    )

    st.subheader("Job Skills")
    st.write(job_skills)

    st.subheader("Candidate Skills")
    st.write(candidate_skills)

    st.subheader("Matched Skills")
    st.success(matched_skills)

    st.subheader("Missing Skills")
    st.error(missing_skills)

with tab3:
    st.header("Recruiter Copilot")

    top_candidate = df.iloc[0]

    st.write(
        f"Candidate ID: {top_candidate['candidate_id']}"
    )

    st.write(
        f"Final Score: {top_candidate['final_score']:.2f}"
    )

    st.success("Strong semantic match")
    st.success("High trust score")
    st.success("Relevant experience")
    st.success("Active candidate profile")

    st.info(
        "Recommendation: Proceed to technical interview."
    )

with tab4:
    st.header("Fraud Detection")

    fraud_df = pd.DataFrame({
        "Candidate ID": [
            "CAND_00001",
            "CAND_00002",
            "CAND_00003"
        ],
        "Risk Level": [
            "High",
            "Low",
            "Medium"
        ],
        "Reason": [
            "Too many skills for experience",
            "Normal Profile",
            "Suspicious activity"
        ]
    })

    st.dataframe(
        fraud_df,
        use_container_width=True
    )

    st.warning(
        "Profiles marked High Risk should be manually reviewed."
    )