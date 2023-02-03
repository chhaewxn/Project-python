from gtts import gTTS
from playsound import Playsound
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '나의 텍스트.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')  # text변수의 문자열을 한글로 변환하여 tts 변수에 바인딩
# 3. 텍스트를 음성으로 변환 폴더에 hi.mp3의 파일 이름으로 저장한다.
tts.save("myText.mp3")

playsound("myText.mp3")
