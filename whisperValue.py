import whisper
import os
import sys
import glob


urls = """
https://www.youtube.com/watch?v=alJaltUmrGo

https://www.youtube.com/watch?v=jQOfbObFOCw

https://www.youtube.com/watch?v=uOfonONtIuk

https://www.youtube.com/watch?v=LWPLjg10D2A

https://www.youtube.com/watch?v=k3HUPHMYEJw

https://www.youtube.com/watch?v=k3HUPHMYEJw

https://www.youtube.com/watch?v=H4W3RSmmY_g

https://www.youtube.com/watch?v=BShvYeyMm_Y

https://www.youtube.com/watch?v=UbpoC2Y9DIA

""".split("\n")

urls = [x for x in urls if len(x) > 0]

model = whisper.load_model("base")
for youtube_url in urls:


    # yt = "https://www.youtube.com/watch?v=pT7vRUGeEtA"
    x = set(list(glob.glob("lectures/*.mp4")))
    os.system("yt-dlp --extract-audio --cookies-from-browser chrome --audio-format mp3 {} -o 'lectures/%(title)s.%(ext)s'".format(youtube_url))

    os.system("yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' --write-thumbnail {}  -o 'lectures/%(title)s.%(ext)s'".format(youtube_url))
    # os.system("youtube-dl --cookies-from-browser chrome {} --write-thumbnail --skip-download".format(youtube_url))
    r = set(list(glob.glob("lectures/*.mp4")))
    print("list: ", r)
    filename = list({t for t in r if t not in x})[0].split("/")[-1].partition(".")[0]
    print(filename)
    # "youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' https://www.youtube.com/watch?v=pT7vRUGeEtA --output temp.mp4".format(yt)
    result = model.transcribe('lectures/{}.mp3'.format(filename))
    with open('lectures/{}.txt'.format(filename), 'w') as f:
        f.write(str(result['text']))

    os.system("magick mogrify -format jpeg lectures/*.webp")