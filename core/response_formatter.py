# core/response_formatter.py

from core.risk_engine import analyze_risk
from core.ai_engine import generate_explanation

def process_text(text):
    """
    Central intelligence pipeline.
    """

    # Step 1: Fast risk detection
    risk_result = analyze_risk(text)

    # Step 2: AI explanation
    ai_response = generate_explanation(text)

    # Step 3: Combine everything
    final_output = {
        "risk_level": risk_result["risk_level"],
        "risk_reason": risk_result["risk_reason"],
        "ai_explanation": ai_response
    }

    return final_output
