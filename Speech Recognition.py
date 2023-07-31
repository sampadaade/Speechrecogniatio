import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to listen to the microphone and recognize speech
def listen_to_microphone():
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            print("Sorry, there was an issue with the service; please try again later.")

if _name_ == "_main_":
    listen_to_microphone()
