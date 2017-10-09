This mini-project was made to answer a few questions: are there combinations of songs that sound good together? And by together, I mean played at the exact same time, with no mixing or any audio processing - just playing two songs at once. 


First I had to get the audio files:\
I used this website to turn my Spotify playlists into Youtube playlists: http://www.playlistbuddy.com
Then I used `youtube-dl` to download audio from playlists\

Afterwards, I used https://github.com/scaperot/the-BPM-detector-python to find BPMs and I modified the algorithm to indicate locations of the beats (before, it only gave bpm.)\

With a list of songs and their BPMs, I went to listened to combinations of many different genres and ultimately came to the conclusion, no. Playing two songs at once does not sound good.