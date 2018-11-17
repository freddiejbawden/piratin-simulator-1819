import speech_recognition as sr
import asyncio
import json

async def get_audio(speech_patterns):
    sr.Microphone(device_index=0)

    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)
    print(sr.Microphone.list_microphone_names())

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("start")
        audio = r.listen(source)
    print("finish")
    try:
        parsed_speak = r.recognize_google(audio)
        return parsed_speak
    except sr.RequestError:
        print("API Unavailable!")
    except sr.UnknownValueError:
        print("Unable to process speech")

def parse_speech(audio_text,speech_patterns):
    words = set(audio_text.split(""))
    for k in speech_patterns.keys():
        for utterance in speech_patterns[k]["utterances"]:
            if utterance

if __name__ == "__main__":
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(index,name)
    with open("utterances.json") as f:
        speech_patterns = json.load(f)
    print(speech_patterns)
    print(parse_speech("test",speech_patterns))
    #print(asyncio.run(get_audio()))
