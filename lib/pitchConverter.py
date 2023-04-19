from pydub import AudioSegment
import json

def midiToPitch(note, octave):
    midiNum = (octave + 1) * 12 + (note - 1)
    pitch = 440 * pow(2, (midiNum - 69) / 12)
    return pitch
def note(name):
    octave = int(name[-1])
    PITCHES = "c,c#,d,d#,e,f,f#,g,g#,a,a#,b".split(",")
    pitch = PITCHES.index(name[:-1].lower())
    return 440 * 2 ** ((octave - 4) + (pitch - 9) / 12.)

def merge_mp3_files(file_list, output_file):
    combined = AudioSegment.empty()
    for file in file_list:
        sound = AudioSegment.from_mp3(file)
        combined += sound
    combined.export(output_file, format="mp3")

def pitchConverter(text):
    with open("tsmmidi", "r") as f:
        midiFile = json.load(f)

    for i, j in zip(text, midiFile):
            originalFile = AudioSegment.from_mp3(f"ttsMp3\\{i}.mp3")
            conversionFile = originalFile.pitch_semitones(midiToPitch(int(j[0]),int(j[1])))
            conversionFile.export(f"pitchCorrection/{i}.mp3", format="mp3")