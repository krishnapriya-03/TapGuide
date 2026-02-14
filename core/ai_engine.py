# core/ai_engine.py

import subprocess

def generate_explanation(text):
    """
    Sends system message to Ollama (phi3:mini)
    and gets structured explanation.
    """

    prompt = f"""
You are a system safety assistant.

Explain the following system message to a non-technical user.

Message:
{text}

Provide:
1. What this means
2. Risk level (Low/Medium/High)
3. What might happen
4. Recommendation

Keep response clear and under 120 words.
"""

    try:
        result = subprocess.run(
            ["ollama", "run", "phi3:mini"],
            input=prompt,
            capture_output=True,
            text=True
        )

        return result.stdout.strip()

    except Exception as e:
        return f"AI processing error: {str(e)}"
