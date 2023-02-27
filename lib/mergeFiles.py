from pydub import AudioSegment

def mergeFiles(text):
    fileList = []
    for i in text:
        fileList.append(AudioSegment.from_file(f"pitchCorrection/{i}.mp3", format="mp3"))
    combined = sum(fileList)
    combined.export("output.mp3", format="mp3")