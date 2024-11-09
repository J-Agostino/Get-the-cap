from youtube_transcript_api import YouTubeTranscriptApi
import re

def clean_text(text):
  """Cleans text extracted from captions.

  Args:
    text: The text to be cleaned.

  Returns:
    The cleaned text.
  """
  # You can customize the cleaning logic here
  # For example, remove punctuation or extra spaces
  cleaned_text = text.strip()  # Remove leading/trailing whitespaces
  return cleaned_text

# Get user input
print("Get the captions for any video\n")
request = input("Enter the URL: ")
lang = input("Langauge for the captions?\n Write es for spanish or en for english: ")

# Extract video ID and validate language
video_id = request.split("?v=")[1].strip()
valid_langs = ["es", "en"]
if lang not in valid_langs:
  print(f"Error: Invalid language code '{lang}'. Please enter 'es' or 'en'.")
  exit()  # Exit program if language is invalid

# Ensure video_id is a string
if not isinstance(video_id, str):
  print("Error: Extracted video ID is not a string.")
  exit()  # Exit program if video ID is not valid

# Download transcript and create temporary list
print(f"Downloading captions in '{lang}'...")
srt = YouTubeTranscriptApi.get_transcript(video_id, languages=[f"{lang}"])

# Clean and store captions in a list
cleaned_captions = []
for item in srt:
  text = item['text']
  cleaned_text = clean_text(text)
  cleaned_captions.append(cleaned_text)

# Write cleaned captions to subtitles.txt
file_name = input("How's your subtitles file is going to be named? ")
print(f"Writing captions to {file_name}.txt...")
with open(f"{file_name}.txt", "w") as f:
  for caption in cleaned_captions:
    f.write(f"{caption}\n")

print("Captions downloaded and cleaned successfully!")