import numpy as np
def calculate_readiness_score(student_vec , centriod , max_distance):
    dist = np.linalg.norm(student_vec - centriod)
    readiness_score = 1 - (dist / max_distance)
    return round(max(0 , min(readiness_score , 1)) * 100 , 2)

def ai_proof_score(aptitude , english , domain_skill):
    weights = {"aptitude": 0.3, "english": 0.3, "domain": 0.4}
    score = (aptitude * weights["aptitude"] + english * weights["english"] + domain_skill * weights["domain"])
    return round((score / 5) * 100, 2)
