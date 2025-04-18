import subprocess
import json

def run_llm(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'mistral'],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

def extract_event_with_llm(text):
    prompt = f'''
Extract any calendar events from the following newsletter. Return a JSON array with:
- summary
- date (YYYY-MM-DD)
- start_time (HH:MM in 24-hour format)
- end_time (optional)
- location
- description (optional)

Newsletter:
---
{text}
---
'''
    response = run_llm(prompt)
    try:
        return json.loads(response.strip())
    except json.JSONDecodeError:
        print("Could not parse LLM response:", response)
        return []
