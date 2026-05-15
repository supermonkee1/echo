from ddgs import DDGS
from commands import chat

def run(query):

    results_text = ""

    with DDGS() as ddgs:

        results = list(ddgs.text(query, max_results=3))

    for result in results:

        title = result.get("title", "")
        body = result.get("body", "")

        results_text += f"{title}\n{body}\n\n"

    prompt = f"""
Answer this question briefly and clearly using these search results.

Question:
{query}

Search Results:
{results_text}
"""

    response = chat.run(prompt)

    return response