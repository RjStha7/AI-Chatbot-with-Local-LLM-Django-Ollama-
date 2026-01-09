import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"

def ask_ai(prompt):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()

        data = response.json()

        # Safe extraction
        if "message" in data and "content" in data["message"]:
            return data["message"]["content"]
        else:
            return f"Unexpected response format: {data}"

    except requests.exceptions.ConnectionError:
        return "Error: Ollama server is not running."
    except Exception as e:
        return f"Error communicating with AI: {str(e)}"
