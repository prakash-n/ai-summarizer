from summarize.ollama_client import generate

def combine_summaries(summaries):
    combined = "\n".join(summaries)
    prompt = f"Combine these into a clear final summary:\n\n{combined}"
    return generate(prompt)