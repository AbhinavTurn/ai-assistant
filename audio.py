from openai import OpenAI
import speech_recognition as sr
import pyttsx3
import time

# Set your OpenAI API key
client = OpenAI(api_key="api-key")  # Replace with your actual key

# Initialize recognizer and text-to-speech
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to listen, send to ChatGPT, and speak response
def listen_and_respond():
    with sr.Microphone() as source:
        print("🎙️ Listening for your question...")
        audio = recognizer.listen(source)

        try:
            # Transcribe speech to text
            question = recognizer.recognize_google(audio)
            print(f"🗣️ You asked: {question}")

            # Send to ChatGPT using updated SDK
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a red team interview assistant. Answer briefly, clearly, and professionally."},
                    {"role": "user", "content": question}
                ]
            )

            answer = response.choices[0].message.content
            print(f"🤖 ChatGPT: {answer}")

            # Speak the answer
            tts_engine.say(answer)
            tts_engine.runAndWait()

        except sr.UnknownValueError:
            print("⚠️ Couldn't understand your voice.")
        except Exception as e:
            print(f"❌ Error: {e}")

# STEP 4: Loop to keep listening
while True:
    listen_and_respond()
    print("⏳ Waiting 5 seconds before next question...\n")
    time.sleep(5)
