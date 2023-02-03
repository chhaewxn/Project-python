import qrcode

# project4_creating_QRcode 폴더에 qrcode_list.txt 파일을 읽는다.
file_path = r'project4_creating_QRcode\qrcode_list.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_lines = f.readlines()  # readlines()로 파일을 읽어 줄 별로 리스트 값의 형태로 내어준다.

    for line in read_lines:
        line = line.strip()  # line.strip()는 줄 마지막에 줄바꿈 문자를 삭제한다.
        print(line)
