job_skills = {
    "AWS",
    "Docker",
    "Terraform",
    "Kubernetes"
}

candidate_skills = {
    "AWS",
    "Docker",
    "Linux"
}

matched_skills = (
    job_skills.intersection(
        candidate_skills
    )
)

missing_skills = (
    job_skills.difference(
        candidate_skills
    )
)

print("\nJob Skills")
print(job_skills)

print("\nCandidate Skills")
print(candidate_skills)

print("\nMatched Skills")
print(matched_skills)

print("\nMissing Skills")
print(missing_skills)