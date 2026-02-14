from core.ai_engine import generate_explanation

sample_text = "This application requires administrator privileges to continue."

response = generate_explanation(sample_text)

print("\nAI RESPONSE:\n")
print(response)
