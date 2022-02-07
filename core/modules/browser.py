import webbrowser
from core.main import speak

def web(query):

    if 'open youtube' in query:
        speak('opening youtube for u')
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        speak('opening google for u')
        webbrowser.open("google.com")
    
    elif 'open stackoverflow' in query:
        speak('opening stackoverflow for u')
        webbrowser.open("stackoverflow.com")
    
    elif 'open github' in query:
        speak('opening github for u')
        webbrowser.open("github.com")
    