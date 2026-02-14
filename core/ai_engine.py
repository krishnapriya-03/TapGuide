# core/ai_engine.py

import subprocess

def generate_explanation(text):
    """
    Sends system message to Ollama (phi3:mini)
    and gets structured explanation.
    """

    prompt = f"""
You are a Windows system safety assistant.

Explain the system message below in simple language for a non-technical or elderly user.

{text}

Respond strictly in this format:

SUMMARY:
(1–2 short sentences explaining what it means)

RISK LEVEL:
(Low / Medium / High)

WHY THIS MATTERS:
(One short sentence)

SAFE STEPS:
1.
2.
3.

Keep it under 60 words.
Do not add extra commentary.
Be calm and clear.

"""


    try:
        result = subprocess.run(
            ["ollama", "run", "phi3:mini"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            
        )

        return result.stdout.strip()

    except Exception as e:
        return f"AI processing error: {str(e)}"
