# core/ai_engine.py
import ollama

def generate_explanation(conversation_history):
    """
    Sends a conversation history to Ollama (phi3:mini) and streams the response.
    The conversation_history is a list of dictionaries, e.g.:
    [{"role": "system", "content": "You are..."}, {"role": "user", "content": "..."}]
    """
    try:
        stream = ollama.chat(
            model='phi3:mini',
            messages=conversation_history,
            stream=True,
        )
        for chunk in stream:
            yield chunk['message']['content']
            
    except Exception as e:
        yield f"AI processing error: {str(e)}"
