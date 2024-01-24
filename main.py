import win32com.client
import speech_recognition as sr
import webbrowser
from openai import OpenAI


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
def AI(prompt):
    client = OpenAI(api_key="your api key")

    

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=1,    
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response)
    
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't get that. Could you please repeat?")
            return ""
        except sr.RequestError as e:
            print(f"Speech recognition request failed: {e}")
            return ""

if __name__ == "__main__":
    print("*All Well*")
    say("Hello, I am your AI")

    # while True:
    text = takeCommand()
    sites=[["youtube","https://www.youtube.com"],["google","https://www.google.com"],["wikipedia","https://www.wikipedia.com"]]

    for site in sites:
        if f"open {site[0]}" in text.lower():
            say(f"Opening {site[0]} for you")
            webbrowser.open(site[1])
        

        if "hyy".lower() in text.lower():

            ai_response = AI(prompt=text)
            print(f"AI Response: {ai_response}")
            say(ai_response)

