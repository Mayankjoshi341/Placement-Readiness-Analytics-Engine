import pandas as pd
def salary_estimation(student_row):
    level = student_row["readiness_level"]

    if level == "Not Ready":
        base_min , base_max = 1.0 , 2.5
    elif level == "Almost Ready":
        base_min , base_max = 2.5 , 5.0
    else:
        base_min , base_max = 4.0 , 5.5
    
    college_factor = 0.0
    if student_row["college_tier"] == "Tier 1":
        college_factor +=20.0
    elif student_row["college_tier"] == "Tier 2":
        college_factor += 5.0
    else:
        college_factor += 0.0
    
    experience_factor = 0.0
    if student_row["internship_count"] >= 1:
        experience_factor += 0.5
    if student_row["applied_work_count"] >= 3:
        experience_factor += 0.5
    if student_row["domain_skill_level"] >= 4:
        experience_factor += 0.5
    


def growth_trajectory(student_row: pd.Series):
    level = student_row["readiness_level"]

    if level == "Not Ready":
        return [
            "Skill Foundation Phase (0-8 months)",
            "Intern / Trainee Roles",
            "Junior Role (1-2 years)",
        ]
    elif level == "Almost Ready":
        return [
            "Junior / Graduate Trainee",
            "Mid-level Role (1-2 years)",
            "Specialist / Lead Track",
        ]
    else:
        return [
            "Direct Entry-Level Role",
            "Strong Mid-level Role (1-2 years)",
            "Advanced / Specialized Track",
        ]
def estimated_time(readiness_score):
    if readiness_score < 40:
        return "6-9 months"
    elif readiness_score < 70:
        return "4-6 months"
    return "1-3 months"


def estimated_impact(focus_areas):
    impact = {}
    for area in focus_areas:
        if area in ["aptitude_level", "domain_skill_level"]:
            impact[area] = "High impact on shortlisting"
        elif area in ["internships_count", "applied_work_count"]:
            impact[area] = "Medium impact on profile"
        else:
            impact[area] = "Supportive improvement"
    return impact

def peer_benchmark(student_row, cluster_profile, feature_cols):
    cluster = student_row["cluster"]
    peer_avg = cluster_profile.loc[cluster, feature_cols]

    comparison = {}
    for f in feature_cols:
        if student_row[f] > peer_avg[f]:
            comparison[f] = "Above average"
        elif student_row[f] < peer_avg[f]:
            comparison[f] = "Below average"
        else:
            comparison[f] = "Average"
    return comparison
