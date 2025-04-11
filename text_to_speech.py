import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    # Set speaking rate and volume
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    # Get voices
    voices = engine.getProperty('voices')

    # Force Microsoft David (male voice)
    for voice in voices:
        if "David" in voice.name:
            engine.setProperty('voice', voice.id)
            print("✅ Using voice:", voice.name)
            break
    else:
        print("⚠️ Microsoft David not found. Using default voice.")

    # Speak
    print("🔊 Speaking...")
    engine.say(text)
    engine.runAndWait()
    print("✅ Done.")

# Main
if __name__ == "__main__":
    print("=== Text to Speech (Male Voice) ===")
    user_input = input("Enter text to speak: ")
    text_to_speech(user_input)
  
    # cd "C:\Users\Pooja D K\OneDrive\Desktop\python project"
#.\env\Scripts\activate
#python text_to_speech.py

