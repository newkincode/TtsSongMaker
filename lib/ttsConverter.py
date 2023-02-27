import gtts
def converter(text):
    for i in text:
        comment_to_voice = gtts.gTTS(text=i, lang="ko")
        comment_to_voice.save(f"ttsMp3/{i}.mp3")

