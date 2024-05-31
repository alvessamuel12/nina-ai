import os
import google.cloud.texttospeech as tts

# Constant paths from files
UTILS_FILE_PATH = './util_p.txt'
START_LISTEN_SOUND_PATH = 'audios/din-ding-89718.mp3'
STOP_LISTEN_SOUND_PATH = 'audios/ringtone-1-46486.mp3'

def fix_response(response):
    response = response.replace('==================================', '\n')
    response = response.replace('Ai Message', '')
    with open(UTILS_FILE_PATH, 'w') as file:
        file.write(response)
        file.close()
    
    with open(UTILS_FILE_PATH, 'r') as file:
        text = file.read()
        print(text)
        file.close()
        os.remove('util_p.txt')
        return text
    
def list_voices(language_code=None):
    client = tts.TextToSpeechClient()
    response = client.list_voices(language_code=language_code)
    voices = sorted(response.voices, key=lambda voice: voice.name)

    print(f" Voices: {len(voices)} ".center(60, "-"))
    for voice in voices:
        languages = ", ".join(voice.language_codes)
        name = voice.name
        gender = tts.SsmlVoiceGender(voice.ssml_gender).name
        rate = voice.natural_sample_rate_hertz
        print(f"{languages:<8} | {name:<24} | {gender:<8} | {rate:,} Hz")