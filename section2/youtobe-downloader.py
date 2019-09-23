import pytube
import os
import subprocess

yt = pytube.YouTube("https://www.youtube.com/watch?v=H36N7BugdDE") # 다운받을 지점
videos = yt.streams.all()

for i in range(len(videos)) :
    print(i, ' , ', videos[i])


cNum = int(input("다운 받을 화질은?"))

down_dir = "C:\youtube"

videos[cNum].download(down_dir)

newFileName = input("변활 할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call([
    'ffmpeg'
    , '-i'
    , os.path.join(down_dir, oriFileName)
    , os.path.join(down_dir, newFileName)
])

print("동영상 다운로드 및 mp3 변환 완료!")
