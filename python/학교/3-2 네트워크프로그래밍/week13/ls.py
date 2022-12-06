import os

# 터미널 실행 경로를 현재 파일 경로로 바꿔주는 명령어
filepath = os.path.dirname(os.path.realpath(__file__))
os.chdir(filepath)


filelist = os.listdir()
for filename in filelist:
    attr = os.stat(filename)
    print(attr)
