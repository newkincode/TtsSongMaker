from pydub import AudioSegment
import numpy as np
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

def pitch_shift(sound, n_steps):
    y = np.frombuffer(sound._data, dtype=np.int16).astype(np.float32)/2**15
    y = librosa.effects.pitch_shift(y, sound.frame_rate, n_steps=n_steps)
    a  = AudioSegment(np.array(y * (1<<15), dtype=np.int16).tobytes(), frame_rate = sound.frame_rate, sample_width=2, channels = 1)
    return a

def change_pitch(input_path, output_path, pitch):
    # Load input file
    sound = AudioSegment.from_file(input_path, format="mp3")

    # Change pitch
    new_sound = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * pitch)
    })

    # Save output file
    new_sound.export(output_path, format="mp3")
    print(output_path)

def pitchConverter(text):
    with open("tsmmidi", "r") as f:
        midiFile = json.load(f)

    for i, j in zip(text, midiFile):
        print(i)
        change_pitch(f"ttsMp3/{i}.mp3",f"pitchCorrection/{i}.mp3",midiToPitch(int(j[0]),int(j[1])))