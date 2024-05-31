import speech_recognition as sr
import keyboard
import os
import pygame
import google.cloud.texttospeech as tts
import time
from typing import Literal
from modules.util import START_LISTEN_SOUND_PATH, STOP_LISTEN_SOUND_PATH


def listen():
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        play_audio(START_LISTEN_SOUND_PATH)
        mic.adjust_for_ambient_noise(source)
        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language='pt-BR')
            play_audio(STOP_LISTEN_SOUND_PATH)
            print("Você disse: " + frase)

            return frase

        except sr.UnknownValueError:
            print("Não entendi... =( ")

def prompt_listen():
        # print('Press Alt Gr and start speaking...')
    print('Pressione Alt Gr e começe a falar...')
    while True:
        if keyboard.is_pressed('alt gr'):
            mic = sr.Recognizer()

            with sr.Microphone() as source:
                play_audio(START_LISTEN_SOUND_PATH)
                mic.adjust_for_ambient_noise(source)

                print("Estou ouvindo...")

                while keyboard.is_pressed('alt gr'):
                    audio = mic.listen(source)

                try:
                    frase = mic.recognize_google(audio, language='pt-BR')
                    play_audio(STOP_LISTEN_SOUND_PATH)
                    print("Você disse: " + frase)

                    return frase

                except sr.UnknownValueError:
                    print("Não entendi... =( ")
                    play_audio(STOP_LISTEN_SOUND_PATH)
                    time.sleep(0.5)
                    play_audio(START_LISTEN_SOUND_PATH)
                    # print('Press Alt Gr and start speaking...')
                    print('Pressione Alt Gr e começe a falar...')

voices = {
    "en-US": {
        "Nora": "en-US-Standard-C",
        "Max": "en-US-Standard-J",
        "Nina": "en-US-Standard-F"
    },
    "pt-BR": {
        "Nora": "pt-BR-Wavenet-A",
        "Max": "pt-BR-Wavenet-B",
        "Nina": "pt-BR-Wavenet-C"
    }
}

def speak(voice_name: Literal["Nora", "Max", "Nina"] = "Nora", text='', language_code : Literal["en-US", "pt-BR"] = "pt-BR"):
    voice_name = voices[language_code][voice_name]
    text_input = tts.SynthesisInput(text=text)
    voice_params = tts.VoiceSelectionParams(
        language_code=language_code, name=voice_name
    )
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    client = tts.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input,
        voice=voice_params,
        audio_config=audio_config,
    )

    filename = f"./audios/{voice_name}.wav"
    with open(filename, "wb") as out:
        out.write(response.audio_content)

    # Pygame audio playback logic
    play_audio(filename)
    os.remove(filename)

def play_audio(filename):
    pygame.init()
    som = pygame.mixer.Sound(filename)
    som.play()
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)
    pygame.quit()