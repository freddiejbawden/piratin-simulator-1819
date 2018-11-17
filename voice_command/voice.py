import speech_recognition as sr
import asyncio
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(index,name)

sr.Microphone(device_index=0)

r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
print(sr.Microphone.list_microphone_names())

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("start")
    audio = r.listen(source)
print("finish")

async def get_speech():
    try:
        parsed_speak = r.recognize_google(audio)
        print(parsed_speak)
    except sr.RequestError:
        print("API Unavailable!")
    except sr.UnknownValueError:
        print("Unable to process speech")
asyncio.run(get_speech())
