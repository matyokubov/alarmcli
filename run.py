import subprocess
import os
import random
from datetime import datetime, timedelta

def parse_time_input(time_str, is_exact_time=True):
    if is_exact_time:
        # Parse time in HH:MM:SS AM/PM format
        time_format = "%I:%M:%S %p"
    else:
        # Parse time in HH:MM:SS format
        time_format = "%H:%M:%S"
    
    return datetime.strptime(time_str, time_format)

def set_alarm_exact_time(alarm_time_str):
    # Get current time
    now = datetime.now()

    # Parse the input time
    alarm_time = parse_time_input(alarm_time_str, is_exact_time=True)

    # Replace the date in alarm_time with the current date
    alarm_time = alarm_time.replace(year=now.year, month=now.month, day=now.day)

    # Determine if the alarm is for today or tomorrow
    if alarm_time <= now:
        # If the time has already passed today, set it for tomorrow
        alarm_time += timedelta(days=1)
        day_str = "tomorrow"
    else:
        day_str = "today"

    # Calculate the time in seconds since the epoch for rtcwake
    epoch_time = int(alarm_time.timestamp())
    print(f"Setting alarm for {day_str} at {alarm_time.strftime('%I:%M:%S %p')}")

    # Run rtcwake command
    rtcwake_cmd = ["sudo", "rtcwake", "-m", "mem", "-l", "-t", str(epoch_time)]
    subprocess.run(rtcwake_cmd)

    # Play a random song after waking up
    play_random_song()

def set_alarm_after_duration(duration_str):
    # Parse the duration
    duration = parse_time_input(duration_str, is_exact_time=False)
    now = datetime.now()

    # Calculate the alarm time
    alarm_time = now + timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)
    day_str = "today" if alarm_time.day == now.day else "tomorrow"

    # Calculate the time in seconds since the epoch for rtcwake
    epoch_time = int(alarm_time.timestamp())
    print(f"Setting alarm for {day_str} at {alarm_time.strftime('%I:%M:%S %p')}")

    # Run rtcwake command
    rtcwake_cmd = ["sudo", "rtcwake", "-m", "mem", "-l", "-t", str(epoch_time)]
    subprocess.run(rtcwake_cmd)

    # Play a random song after waking up
    play_random_song()

def play_random_song():
    # Directory containing songs
    songs_dir = "songs"

    # List all mp3 files in the directory
    songs = [f for f in os.listdir(songs_dir) if f.endswith('.mp3')]

    if not songs:
        print("No songs found in the 'songs' directory.")
        return

    # Select a random song
    random_song = random.choice(songs)
    song_path = os.path.join(songs_dir, random_song)

    print(f"Playing song: {random_song}")

    # Run mpv to play the song
    mpv_cmd = ["mpv", song_path]
    subprocess.run(mpv_cmd)

def main():
    print("Choose an option:")
    print("1. Set an alarm for an exact time")
    print("2. Set an alarm after a certain duration")

    choice = input("> ").strip()

    if choice == '1':
        alarm_time_str = input("Enter the alarm time (HH:MM:SS AM/PM): ").strip()
        set_alarm_exact_time(alarm_time_str)
    elif choice == '2':
        duration_str = input("Enter the duration (HH:MM:SS): ").strip()
        set_alarm_after_duration(duration_str)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

