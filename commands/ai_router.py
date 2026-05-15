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
- ask_web

If the user wants Echo to perform an action on the computer, ALWAYS choose a tool action.

Only use ask_web for factual questions or information requests, or unknown for jokes, casual conversation,
or anything that doesn't fit the other categories.    

Look first for keywords in the user's request to determine the action, but if it's not clear, use your best judgement to choose the
most likely action based on the content of the request. Don't be afraid to use "unknown" if you're not sure, but try to choose 
the most specific action possible when you can.  

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

User: capture the screen
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
{"action":"ask_web","query":"python tutorials"}

User: look up the weather
Response:
{"action":"ask_web","query":"The weather"}

User: who made minecraft
Response:
{"action":"ask_web","query":"who made minecraft"}

User: what is the capital of france
Response:
{"action":"ask_web","query":"The capital of france"}

User: look up cricket matches tomorrow
Response:
{"action":"ask_web","query":"cricket matches tomorrow"}

User: what is the weather tomorrow
Response:
{"action":"ask_web","query":"weather tomorrow"}

User: latest minecraft update
Response:
{"action":"ask_web","query":"latest minecraft update"}

User: today's news
Response:
{"action":"ask_web","query":"today news"}

User: who won the football match yesterday
Response:
{"action":"ask_web","query":"football match yesterday"}

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