from pydub import AudioSegment
import librosa
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

# change_pitch
def change_pitch(input_file, output_file, pitch):
    y, sr = librosa.load(input_file)
    y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=pitch)
    librosa.output.write_wav(output_file, y_shifted, sr)

def pitchConverter(text):
    with open("tsmmidi", "r") as f:
        midiFile = json.load(f)

    for i, j in zip(text, midiFile):
        print(i)
        change_pitch(f"ttsMp3/{i}.mp3",f"pitchCorrection/{i}.mp3",midiToPitch(int(j[0]),int(j[1])))