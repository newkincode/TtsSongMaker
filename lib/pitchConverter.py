from pydub import AudioSegment
import json

def midiToPitch(note, octave):
    midiNum = (octave + 1) * 12 + (note - 1)
    pitch = 440 * pow(2, (midiNum - 69) / 12)
    return pitch

def pitchConverter(text):
    with open("tsmmidi.json", "r") as f:
        midiFile = json.load(f)

    for i in text:
        for j in midiFile:
            originalFile = AudioSegment.from_mp3(f"ttsMp3/{i}.mp3")
            conversionFile = originalFile.pitch_semitones(midiToPitch(int(j[0]),int(j[1])))
            conversionFile.export(f"pitchCorrection/{i}.mp3", format="mp3")