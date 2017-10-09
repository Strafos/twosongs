from pydub import AudioSegment

filename1 = 'Disturbed - down with the sickness-L78yVFeyvRo.wav'
filename2 = 'Georges Bizet - Carmen Suite No. 2 - Habanera-4rwcRQvAiTg.wav'
sound1 = AudioSegment.from_mp3(filename1) - 10
sound2 = AudioSegment.from_mp3(filename2) + 20 

# mix sound2 with sound1, starting at 5000ms into sound1)
output = sound2.overlay(sound1, position=300)

# save the result
output.export("mixed_sounds.wav", format="wav")
