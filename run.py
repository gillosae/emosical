import os
import subprocess
import sys

import srt
from tqdm import tqdm

import demucs.demucs.htdemucs as htdemucs

# Alias the module so that unpickling can find 'demucs.htdemucs'
sys.modules["demucs.htdemucs"] = htdemucs
from demucs.demucs import separate

opj = os.path.join

theatre_dir = "data/raw/theatre"
audio_dir = "data/audio"
video_dir = "data/video"
movies_file = "movies.txt"
ALLOWED_EXTENSIONS = [".mp4", ".mkv"]


# Check existing movies
def check_files():
    # Alert if the theatre directory does not exist
    if not os.path.exists(theatre_dir):
        print(f"Alert: Directory '{theatre_dir}' does not exist!")
        return

    # Read movie list from movies.txt
    try:
        with open(movies_file, "r") as f:
            movies = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Movies file '{movies_file}' not found!")
        return

    # Check existence of each movie file in the theatre directory
    existing_movies = []
    missing_movies = []

    for movie in movies:
        found = False
        for ext in ALLOWED_EXTENSIONS:
            movie_file = movie + ext
            movie_path = opj(theatre_dir, movie_file)
            if os.path.isfile(movie_path):
                existing_movies.append(movie_file)
                found = True
                break  # stop checking other extensions if found
        if not found:
            missing_movies.append(movie)

    if existing_movies:
        print("Existing movies:")
        for movie in existing_movies:
            print(" -", movie)
        if len(missing_movies) != 0:
            print("\nMissing movies:")
        for movie in missing_movies:
            print(" -", movie)
        print(f"\nProceed with {len(existing_movies)} movie(s).")
    else:
        print("No movies exist in the directory 'data/raw/theatre'.")
        # If no movies exist, check whether corresponding subtitle files (.srt) exist.
        matching_srt = []
        for movie in movies:
            base, _ = os.path.splitext(movie)
            srt_filename = base + ".srt"
            srt_path = opj(theatre_dir, srt_filename)
            if os.path.isfile(srt_path):
                matching_srt.append(srt_filename)
        if matching_srt:
            print("However, found matching subtitle files for the following movies:")
            for srt in matching_srt:
                print(" -", srt)
        else:
            print("No matching subtitle files found either.")

    return existing_movies


# Parse audio, video
def parse_av_ffmpeg(movie):
    print(f"Parsing audio/video for file: {movie}")
    # Use theatre_dir to locate the movie file
    movie_path = opj(theatre_dir, movie)
    # Derive the base name (without extension) for folder naming
    movie_name = os.path.splitext(os.path.basename(movie_path))[0]

    # Build the path to the corresponding SRT file
    srt_path = opj("data", "raw", "srt", movie_name + ".srt")
    if not os.path.isfile(srt_path):
        print(f"Subtitle file not found: {srt_path}")
        return

    # Parse the SRT file
    try:
        with open(srt_path, "r", encoding="utf-8") as f:
            srt_content = f.read()
        subtitles = list(srt.parse(srt_content))
    except Exception as e:
        print(f"Error parsing SRT file: {e}")
        return

    # Create output directories for audio and video segments
    audio_output_dir = opj(audio_dir, movie_name)
    video_output_dir = opj(video_dir, movie_name)
    os.makedirs(audio_output_dir, exist_ok=True)
    os.makedirs(video_output_dir, exist_ok=True)

    # Process each subtitle segment
    for i, sub in enumerate(tqdm(subtitles, desc="Extracting segments"), start=1):
        start_time = sub.start.total_seconds()
        end_time = sub.end.total_seconds()
        duration = end_time - start_time

        # Build output filenames
        audio_output_file = opj(audio_output_dir, f"{i}.wav")
        video_output_file = opj(video_output_dir, f"{i}.mp4")

        # Extract audio segment (re-encode to WAV)
        audio_command = [
            "ffmpeg",
            "-ss",
            str(start_time),
            "-t",
            str(duration),
            "-i",
            movie_path,
            "-vn",  # no video
            "-acodec",
            "pcm_s16le",  # WAV audio
            audio_output_file,
            "-y",
        ]
        subprocess.run(
            audio_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )

        # Extract video segment (copy streams for speed)
        video_command = [
            "ffmpeg",
            "-ss",
            str(start_time),
            "-t",
            str(duration),
            "-i",
            movie_path,
            "-c",
            "copy",
            video_output_file,
            "-y",
        ]
        subprocess.run(
            video_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )


# Vocal separation
def demucs_audio_processing(file_path):
    print(f"Demucs audio processing for file: {file_path}")

    # Run Demucs to separate only vocals using the --two-stems=vocals flag.
    # This is equivalent to: demucs --two-stems=vocals myfile.mp3
    separate.main(["--two-stems=vocals", file_path])


def demucs_audio_processing(file_path):
    print(f"Demucs audio processing for file: {file_path}")

    # Derive the movie name from the audio file's parent directory.
    movie_name = os.path.basename(os.path.dirname(file_path))
    output_dir = os.path.join("data", "audio_demucs", movie_name)
    os.makedirs(output_dir, exist_ok=True)

    # Run Demucs to separate only vocals (using --two-stems=vocals)
    # and direct the output to the corresponding folder.
    separate.main(["--two-stems=vocals", "--out", output_dir, file_path])


# Speech enhancement
def sgmse_audio_processing(file_path):
    print(f"SE audio processing for file: {file_path}")


if __name__ == "__main__":
    # existing_movies = check_files()
    # for movie in existing_movies:
    #     parse_av_ffmpeg(movie)

    # Perform demucs on all audio at /data/audio/{movie_name}/{index}.wav
    # and save to /data/audio_demucs/{movie_name}/{index}.wav

    # Now, process all audio segments in data/audio/{movie_name}/{index}.wav with Demucs.
    for movie_name in os.listdir(audio_dir):
        movie_audio_dir = opj(audio_dir, movie_name)
        if os.path.isdir(movie_audio_dir):
            for file in os.listdir(movie_audio_dir):
                if file.lower().endswith(".wav"):
                    file_path = opj(movie_audio_dir, file)
                    demucs_audio_processing(file_path)
