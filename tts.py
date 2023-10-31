import os
import uuid
import requests

from typing import List
from moviepy.editor import *

def split_into_sentences(text: str) -> List[str]:
    """
    Splits a text into a list of sentences.
    """
    return text.split(".")

def create_random_id() -> str:
    """
    Create a random ID for the audio file.
    """
    return str(uuid.uuid4())

def generate_tts(text: str) -> str:
    """
    Generate TTS for a text and return file path.
    """
    voice = "adam"
    output = f"audio/tts/{create_random_id()}.mp3"

    if os.path.exists(output):
        os.remove(output)

    print("Generating TTS...")
    r = requests.get(f"https://api.pawan.krd/tts?text={text}&voice={voice}")

    if r.status_code != 200:
        print(r.json())

    with open(output, "wb") as f:
        f.write(r.content)

    print("Done!")

    return output

def combine_audio_sounds(tts_files: List[str]) -> str:
    """
    Combine multiple audio files into one.
    """
    print("Combining audio files...")
    audio_clips = [AudioFileClip(tts_file) for tts_file in tts_files]
    final_clip = concatenate_audioclips(audio_clips)
    final_clip.write_audiofile("final.mp3")
    print("Done!")

    return "final.mp3"

text = "DID YOU KNOW that the AI industry is worth 15.7 Trillion dollars, and is STILL growing!"

#sentences = split_into_sentences(text)

generate_tts(text)

#final_audio = combine_audio_sounds(tts_files)