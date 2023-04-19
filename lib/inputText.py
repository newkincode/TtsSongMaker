import json
def inputFile():
    with open("tsmmidi", "w") as f:
        json.dump(list(input("음표를 입력하세요 띄어쓰기로 구분, 도:1레:2 같은 숫자 + 옥타브 예) 11(1옥타브 도) : ").split()), f)