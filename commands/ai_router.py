import requests
import json

PROMPT = """
You are Echo's intent parser.

Your job is to convert user requests into JSON actions.

Only return VALID JSON.

Allowed actions:
- open_app
- screenshot
- sleep
- unknown
- search_web

Examples:

User: open chrome
Response:
{"action":"open_app","target":"chrome"}

User: launch my browser
Response:
{"action":"open_app","target":"chrome"}


User: take a screenshot
Response:
{"action":"screenshot"}


User: go to sleep.
Response:
{"action":"sleep"}


User: tell me a joke
Response:
{"action":"unknown"}



User: search for python tutorials
Response:
{"action":"search_web","query":"python tutorials"}

User: look up the weather
Response:
{"action":"search_web","query":"weather"}
"""

def run(command):

    full_prompt = f"{PROMPT}\n\nUser: {command}"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": full_prompt,
            "stream": False
        }
    )

    data = response.json()

    raw_text = data["response"].strip()

    
    

    try:

        start = raw_text.find("{")
        end = raw_text.rfind("}") + 1

        json_text = raw_text[start:end]

        parsed = json.loads(json_text)

        return parsed

    except:

        return {
            "action": "unknown"
        }