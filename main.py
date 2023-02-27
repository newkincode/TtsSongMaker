import os
import lib.inputText as it
import lib.mergeFiles as mf
import lib.pitchConverter as pc
import lib.ttsConverter as tc

if os.path.exists("ttsMp3"):
    for f in os.listdir("ttsMp3"):
        os.remove(os.path.join("ttsMp3", f))
else:
    os.mkdir("ttsMp3")
    
if os.path.exists("pitchCorrection"):
    for f in os.listdir("pitchCorrection"):
        os.remove(os.path.join("pitchCorrection", f))
else:
    os.mkdir("pitchCorrection")

it.inputFile()
text = input("가사를 입력하세요 가사에 띄어쓰기가 있으면 안되고, 같은 글자가 들어가면 안됩니다 예) 가나다라가나다(가나다 가 두게 들어갔기때문에 안됨) : ")
tc.converter(text)
pc.pitchConverter(text)


if os.path.exists("ttsMp3"):
    for f in os.listdir("ttsMp3"):
        os.remove(os.path.join("ttsMp3", f))
else:
    os.mkdir("ttsMp3")
    
if os.path.exists("pitchCorrection"):
    for f in os.listdir("pitchCorrection"):
        os.remove(os.path.join("pitchCorrection", f))
else:
    os.mkdir("pitchCorrection")