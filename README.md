# YouTube-Audio-Playlist-Downloader
This code is a Python program that downloads audio files from a YouTube playlist
. The program starts by asking the user to enter the URL of the YouTube playlist. 
Then, it uses the pytube library to extract the videos from the playlist and download
the audio from each video. The audio files are stored in a directory named "audio_files".
The program also includes a check to see if the audio files already exist, and if 
they do, the program skips downloading them. After the audio files have been downloaded,
the program gives the user the option to delete the audio files after they have been 
played. The program uses the os and shutil libraries to handle file and directory 
operations, and the time library to measure the download time. The code also includes
comments to explain what each section of the code is doing.
