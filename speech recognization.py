import speech_recognition as sr

# Create a Recognizer object
recognizer = sr.Recognizer()

# Use the microphone as the audio source
try:
    with sr.Microphone() as source:
        print("Microphone is active. Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)
        print("Recording complete, recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
except sr.RequestError as e:
    print("API unavailable or unresponsive:", e)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except Exception as e:
    print("Microphone not found or other error:", e)
