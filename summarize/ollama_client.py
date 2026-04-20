import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def generate(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        if "response" not in data or not data["response"].strip():
            return None

        return data["response"]

    except Exception:
        return None


def generate_summary(chunk, mode="brief"):
    prompts = {
        "very short": "Summarize this in exactly ONE short sentence. No extra explanation.",
        "brief": "Summarize in 3-4 clear sentences.",
        "bullet": "Summarize into concise bullet points.",
        "detailed": "Provide a detailed and structured summary.",
        "insights": "Extract key insights and takeaways."
    }

    prompt = f"{prompts.get(mode, prompts['brief'])}\n\n{chunk}"

    return generate(prompt)