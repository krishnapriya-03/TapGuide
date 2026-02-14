def analyze_risk(text):
    text_lower = text.lower()
    risk_keywords = {
          "delete": "HIGH",
        "format": "CRITICAL",
        "administrator": "MEDIUM",
        "erase": "CRITICAL",
        "remove": "HIGH",
        "firewall": "MEDIUM",
        "restart": "LOW",
        "install": "LOW",
        "allow": "MEDIUM"
    }

    detected_risk="LOW"
    detected_reason = "No high-risk keywords detected."

    for keyword, risk_level in risk_keywords.items():
        if keyword in text_lower:
            detected_risk = risk_level
            detected_reason = f"Detected keyword: '{keyword}' with risk level: {risk_level}."
            break

    return{
        "risk_level":detected_risk,
        "risk_reason": detected_reason
    }