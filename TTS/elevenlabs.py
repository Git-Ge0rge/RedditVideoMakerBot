import random

from elevenlabs import generate, save

from utils import settings

voices = [
    "Adam",
    "Antoni",
    "Arnold",
    "Bella",
    "Domi",
    "Elli",
    "Josh",
    "Rachel",
    "Sam",
]


class elevenlabs:
    def __init__(self):
        self.max_chars = 2500
        self.voices = voices

    def run(self, text, filepath, random_voice: bool = False):
        if random_voice:
            voice = self.randomvoice()
        else:
            voice = str(settings.config["settings"]["tts"]["elevenlabs_voice_name"]).capitalize()

        if settings.config["settings"]["tts"]["elevenlabs_api_key"]:
            api_key = settings.config["settings"]["tts"]["elevenlabs_api_key"]
        else:
            raise ValueError(
                "You didn't set an Elevenlabs API key! Please set the config variable ELEVENLABS_API_KEY to a valid API key."
            )

        audio = generate(api_key=api_key, text=text, voice=voice, model="eleven_multilingual_v1")
        save(audio=audio, filename=filepath)

    def randomvoice(self):
        return random.choice(self.voices)

#CHATGPT Adjustment for ID 
# import random

# # Assuming generate and save functions are defined elsewhere, as in your original code.
# from elevenlabs import generate, save
# from utils import settings

# # Original list of voices, kept for fallback or random selection.
# voices = [
#     "Adam",
#     "Antoni",
#     "Arnold",
#     "Bella",
#     "Domi",
#     "Elli",
#     "Josh",
#     "Rachel",
#     "Sam",
# ]

# class elevenlabs:
#     def __init__(self):
#         self.max_chars = 2500
#         self.voices = voices

#     def run(self, text, filepath, random_voice: bool = False, custom_voice: str = None):
#         """
#         Generate and save audio from text using a specified voice.

#         Parameters:
#         - text: The text to be converted to speech.
#         - filepath: Where to save the generated audio file.
#         - random_voice: If True, select a voice at random. This is ignored if custom_voice is specified.
#         - custom_voice: Optionally specify a custom voice to use. This overrides the random_voice setting.
#         """
#         # Use the custom voice if provided, else fall back to original behavior.
#         if custom_voice:
#             voice = custom_voice
#         elif random_voice:
#             voice = self.randomvoice()
#         else:
#             # Fallback to a voice from settings if no custom voice is provided and random_voice is False.
#             voice = str(settings.config["settings"]["tts"]["elevenlabs_voice_name"]).capitalize()

#         # Check for API key in settings.
#         if settings.config["settings"]["tts"]["elevenlabs_api_key"]:
#             api_key = settings.config["settings"]["tts"]["elevenlabs_api_key"]
#         else:
#             raise ValueError(
#                 "You didn't set an Elevenlabs API key! Please set the config variable ELEVENLABS_API_KEY to a valid API key."
#             )

#         # Generate and save the audio with the selected voice.
#         audio = generate(api_key=api_key, text=text, voice=voice, model="eleven_multilingual_v1")
#         save(audio=audio, filename=filepath)

#     def randomvoice(self):
#         """Select a voice at random from the available voices."""
#         return random.choice(self.voices)


# MY SCRIPT 
# import pandas as pd
# import requests

# # Load the Excel file
# df = pd.read_excel('Reddit_AITA_Posts.xlsx')

# # Function to call ElevenLabs TTS API
# def generate_tts(text, post_id):
#     url = "https://api.elevenlabs.io/v1/text-to-speech/sgOv2ShY7b52jNPhay9M"
#     payload = {
#         "model_id": "eleven_turbo_v2",
#         "text": text,
#         "voice_settings": {
#             "similarity_boost": 123,
#             "stability": 123,
#             "style": 123,
#             "use_speaker_boost": True
#         }
#     }
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "8e23ecb164f834b4a4f366b9e83df306"
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     # Save the response content (audio file) to a file
#     with open(f"narration_{post_id}.mp3", 'wb') as audio_file:
#         audio_file.write(response.content)

# # Generate TTS for each post
# for index, row in df.iterrows():
#     title_content = f"{row['Title']}. {row['Content']}"
#     generate_tts(title_content, index)  # Use DataFrame index as ID for uniqueness

# print("TTS narrations have been generated for each post.")
