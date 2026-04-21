from ..prediction_service.analysis.input_based import aptitude_insight , english_insight , domain_skill_insight
from ..prediction_service.analysis.math_based import calculate_readiness_score , ai_proof_score
from ..prediction_service.analysis.rule_based import growth_trajectory , estimated_time , estimated_impact , salary_estimation , peer_benchmark
from ..prediction_service.analysis.insights import gap_analysis , categorize_gaps , focus_priorities , domain_switch_feasibility , placement_type
import numpy as np
import pandas as pd
def generate_report(student_row , cluster_profile , feature_cols , DOMAIN_SKILL_SCHEMA , DEGREE_ROLE_MAP):
    report = {}
    report["readiness_level"] = student_row["readiness_level"]
    report["aptitude_insight"] = aptitude_insight(student_row["aptitude_level"])
    report["english_insight"] = english_insight(student_row["english_test_answers"])
    report["domain_skill_insight"] = domain_skill_insight(student_row["domain_skill_level"])
    
    student_vec = student_row[feature_cols].values
    centriod = cluster_profile.loc[student_row["cluster"], feature_cols].values
    max_distance = np.linalg.norm(cluster_profile[feature_cols].max().values - cluster_profile[feature_cols].min().values)
    
    report["readiness_score"] = calculate_readiness_score(student_vec, centriod, max_distance)
    report["ai_proof_score"] = ai_proof_score(student_row["aptitude_level"], student_row["english_level"], student_row["domain_skill_level"])
    
    report["growth_trajectory"] = growth_trajectory(student_row)
    report["salary_estimation"] = salary_estimation(student_row)
    report["estimated_time_to_ready"] = estimated_time(report["readiness_score"])
    report["peer_comparison"] = peer_benchmark(student_row, cluster_profile, feature_cols)
    report["estimated_impact"] = estimated_impact(["aptitude_level", "domain_skill_level", "internship_count", "applied_work_count"])
    
    gaps = gap_analysis(student_row, cluster_profile, feature_cols)
    strengths, weaknesses = categorize_gaps(gaps)
    report["strengths"] = strengths.index.tolist()
    report["weaknesses"] = weaknesses.index.tolist()
    report["focus_priorities"] = focus_priorities(weaknesses).index.tolist()
    
    report["domain_switch_feasibility"] = domain_switch_feasibility(student_row["degree"], DOMAIN_SKILL_SCHEMA, DEGREE_ROLE_MAP)
    report["placement_type"] = placement_type(student_row["tenth_percentage"], student_row["twelfth_percentage"], student_row["cgpa"], student_row["domain_skill_level"])
    
    return report