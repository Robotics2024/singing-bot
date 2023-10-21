from gtts import gTTS
from midiutil import MIDIFile

# Lyrics
lyrics = [
    "Five times one is five, come on, give it a swing",
    "Five times two is ten, with a magical ring",
    
]

try:
    # Text-to-Speech (TTS) for vocals
    vocal_track = gTTS(' '.join(lyrics), lang='en', slow=False)
    vocal_track.save('vocals.mp3')
except:
    print("error creating vocal track")

# Music generation with MIDIUtil
MyMIDI = MIDIFile(1)  # Create a MIDI file with one track
MyMIDI.addTempo(0, 0, 120)  # Set tempo

# Add your musical notes and rhythm here using MIDIUtil

# Save the generated music as a MIDI file
with open("music.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
