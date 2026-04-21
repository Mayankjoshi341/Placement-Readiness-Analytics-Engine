def aptitude_insight(score):
    if score >= 4.5:
        return "Excellent aptitude skills, well above average."
    elif score >= 3:
        return "Good aptitude skills, above average."
    elif score >= 2:
        return "Average aptitude skills, room for improvement."
    else:
        return "Below average aptitude skills, needs significant improvement."
    
def english_insight(test : str):
    if len(test)  <= 20:
        return "Limited English proficiency, significant improvement needed."
    elif len(test) <= 50:
        return "Basic English proficiency, needs improvement for professional settings."
    else:
            return "Good English proficiency, suitable for most professional settings."
def domain_skill_insight(score):
    if score >= 4.5:
        return "Exceptional domain knowledge, highly job-ready."
    elif score >= 3:
        return "Strong domain knowledge, good job readiness."
    elif score >= 2:
        return "Basic domain knowledge, needs improvement for job readiness."
    else:
        return "Limited domain knowledge, significant improvement needed for job readiness."
    