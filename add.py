from typing import List
from moviepy.editor import *

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

files = [
    "audio/tts/7af68c49-e3ff-4dde-bdf5-c7f89f3c7350.mp3",
    "audio/tts/bd2372c4-dfc2-437b-b300-ea9b54fe4cb4.mp3",
    "audio/tts/e7aac85f-c241-4d36-a8c4-07f8f0ffcf30.mp3",
    "audio/tts/cc534b1e-57cf-4bf7-a9ef-6b17cec48f3b.mp3",
    "audio/tts/fcfa8b8a-296d-4a11-8b58-0e777cfa77c0.mp3",
    "audio/tts/c5528af1-097f-435b-8d65-241221af87c8.mp3"
]

print(files)

combine_audio_sounds(files)