import io
import json
import pyttsx3
import requests

from moviepy.editor import *
from PIL import Image

HUGGING_FACE_API_KEY = open('api_keys.txt', 'r').read()

ENGINE = pyttsx3.init()

def clean_script_to_file_name(script: str):
    return script.replace(' ', '_').replace('\n', '_').replace('\t', '_').replace('\r', '_').lower()

def generate_images(image_generation_prompts):
    file_paths = []

    headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}

    for prompt in image_generation_prompts:
        # Generate image
        r = requests.post("https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0", headers=headers, json={
            "inputs": prompt 
        })

        # Save image
        image = Image.open(io.BytesIO(r.content))
        file_name = clean_script_to_file_name(prompt)
        file_path = f'./images/{file_name}.png'
        image.save(file_path)

        # Add to list of file paths
        file_paths.append(file_path)

    return file_paths

def combine_tts_and_images(tts_file_path, image_file_paths, output_path):
    # Load TTS audio
    tts_audio = AudioFileClip(tts_file_path)

    # Load images
    image_clips = [ImageClip(image_path, duration=tts_audio.duration) for image_path in image_file_paths]

    # Combine audio and images
    final_video = concatenate_videoclips([tts_audio.set_audio(None).set_duration(tts_audio.duration)] + image_clips, method="compose")

    # Write the combined video to the output path
    final_video.write_videofile(output_path, codec="libx264")

def main():
    scripts = json.load(open('resources.json', 'r', encoding='utf-8'))

    for script in scripts:
        tts_file_path = script['tts_path']
        image_file_paths = generate_images(script['image_generation_prompts'])
        output_path = f'./output_videos/{clean_script_to_file_name(script["text"])}.mp4'
        combine_tts_and_images(tts_file_path, image_file_paths, output_path)

if __name__ == '__main__':
    main()
