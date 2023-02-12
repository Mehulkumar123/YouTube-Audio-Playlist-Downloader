import os
import time
import shutil
from pytube import YouTube, Playlist

# Get the YouTube playlist URL from the user
playlist_url = input("Enter the YouTube playlist URL: ")

# Use the Playlist class from the pytube library to get the videos in the playlist
playlist = Playlist(playlist_url)

# Create a directory to store the audio files
if not os.path.exists("audio_files"):
    os.makedirs("audio_files")

# Loop through all the videos in the playlist
for video_url in playlist:
    # Use the YouTube class from the pytube library to download the audio from the video
    video = YouTube(video_url)
    audio_stream = video.streams.filter(only_audio=True).first()

    # Get the filename for the audio file
    filename = audio_stream.default_filename

    # Store the audio files in the "audio_files" directory
    file_path = os.path.join("audio_files", filename)

    # Check if the file already exists
    if os.path.exists(file_path):
        # If the file exists, skip downloading it
        print(f"{filename} already exists, skipping...")
        continue

    # Display information about the audio file being downloaded
    print(f"Downloading {filename}...")

    # Start a timer to measure the download time
    start = time.time()

    # Download the audio file to the "audio_files" directory
    audio_stream.download(output_path="audio_files")

    # End the timer and calculate the download time
    end = time.time()

    # Display information about the download time
    print(f"{filename} has been successfully downloaded in {end - start:.2f} seconds.")

# Ask the user if they want to delete the audio files after they have been played
delete = input("Do you want to delete the audio files after they have been played? (yes/no) ")

# If the user chooses to delete the audio files, remove the "audio_files" directory and its contents
if delete.lower() == "yes":
    shutil.rmtree("audio_files")
    print("The audio files have been deleted.")

# Display a message to indicate that all the audio files have been downloaded
print("All audio files from the playlist have been successfully downloaded!")
