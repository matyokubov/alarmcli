#!/bin/bash

#Today
#Would you like to set a wake without turning sleep mode on?
# sudo rtcwake -m no -l -t "$(date -d 'today 12:00:00' '+%s')"

#Would you like to set a wake with turning sleep mode on?
# sudo rtcwake -m mem -l -t "$(date -d 'today 12:00:00' '+%s')"

#I wanna set an alarm to get up early tomorrow morning.
#I'm going to sleep. And I would like to wake up whith a song
#To be played the song, you must have 'mpv'
sudo rtcwake -m mem -l -t "$(date -d 'tomorrow 05:30:00' '+%s')" && mpv song_sample.mp3
