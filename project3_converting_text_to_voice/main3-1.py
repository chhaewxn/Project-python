from gtts import gTTS

text = "안녕하세요. 파이썬 프로젝트3 입니다."  # text변수에 문자열을 바인딩한다.

tts = gTTS(text=text, lang='ko')  # text변수의 문자열을 한글로 변환하여 tts 변수에 바인딩
# 3. 텍스트를 음성으로 변환 폴더에 hi.mp3의 파일 이름으로 저장한다.
tts.save(r"3. 텍스트를 음성으로 변환\hi.mp3")
