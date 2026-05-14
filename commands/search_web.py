import webbrowser

def run(query):

    url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)

    return f"Searching for {query}"