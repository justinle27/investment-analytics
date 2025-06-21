def get_risk_profile(score):
    if score <= 10:
        return "Low Risk"
    elif score <= 20:
        return "Moderate Risk"
    else:
        return "High Risk"