import pandas as pd
def gap_analysis(student_row : pd.Series , cluster_profile : pd.DataFrame , feature_cols : list):
    cluster_id = student_row["cluster"]
    cluster_mean = cluster_profile.loc[cluster_id , feature_cols][0]
    return student_row[feature_cols] - cluster_mean

def categorize_gaps(gaps: pd.Series):
    strengths = gaps[gaps > 0.3].sort_values(ascending=False)
    weaknesses = gaps[gaps < -0.3].sort_values()
    return strengths, weaknesses


def focus_priorities(weaknesses: pd.Series, top_n=2):
    return weaknesses.head(top_n)

def domain_switch_feasibility(degree , DOMAIN_SKILL_SCHEMA , DEGREE_ROLE_MAP):
    feasibility = 0.0
    if degree in DEGREE_ROLE_MAP.get(degree , []):
        feasibility = 0.8
    else:
        feasibility = 0.3
    if DOMAIN_SKILL_SCHEMA[degree]["tier"] == "high" and feasibility <= 0.5:
        feasibility -= 0.05
    elif DOMAIN_SKILL_SCHEMA[degree]["tier"] == "low" and feasibility > 0.5:
        feasibility += 0.2
    
    return round(feasibility * 100 , 2)

def placement_type(tenth , twelfth , cgpa , domain_skill_level):
    if tenth >= 70 and twelfth >= 70 and cgpa >= 7.0 and domain_skill_level >= 2:
        return "Target ON-CAMPUS"
    elif tenth < 50 or twelfth < 50 or cgpa < 5.0:
        return "Focus more on OFF-CAMPUS"
    else:
        return "Can target both ON-CAMPUS and OFF-CAMPUS"
    