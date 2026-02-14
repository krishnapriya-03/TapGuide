# core/ai_engine.py

import subprocess

def generate_explanation(text):
    """
    Sends system message to Ollama (phi3:mini)
    and gets structured explanation.
    """

    prompt = f"""
You are a system safety assistant.

Explain the following system message clearly to a non-technical user.

Message:
{text}

Respond strictly in this format:

What This Means:
<2-3 sentence explanation>

Risk Level:
<Low / Medium / High>

Possible Impact:
- Bullet point 1
- Bullet point 2
- Bullet point 3

How To Proceed Safely:
1. Step one
2. Step two
3. Step three

Keep it under 60 words.
Be practical and realistic.
Do not be overly technical.
"""


    try:
        result = subprocess.run(
            ["ollama", "run", "phi3:mini"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=25
        )

        return result.stdout.strip()

    except Exception as e:
        return f"AI processing error: {str(e)}"
