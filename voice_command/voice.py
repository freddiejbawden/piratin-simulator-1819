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
    for k in speech_patterns.keys():
        for ut in speech_patterns[k]["utterances"]:
            split_aud = audio_text.split(" ")
            if all(word in split_aud for word in split_aud):
                try:
                    if speech_patterns[k]["variables"]:
                        for v in speech_patterns[k]["variables"]:
                            if v in split_aud:
                                print(k,v)
                                return(k,v)
                        print("variable not found")
                except:
                    print(k)
                return
    print("no match")

if __name__ == "__main__":
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(index,name)
    with open("utterances.json") as f:
        speech_patterns = json.load(f)
    parse_speech("fire cannons starboard",speech_patterns)
    #print(asyncio.run(get_audio()))
