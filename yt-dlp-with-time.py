import os

def dl_tp(url, start, end):
    os.system(f"yt-dlp -x -f 'ba' --audio-format m4a --external-downloader ffmpeg --external-downloader-args 'ffmpeg_i:-ss {start} -to {end}' -o '~/Downloads/YouTube Videos/50 Anniversary/%(title)s.%(ext)s' {url}")

def dl(url):
    os.system(f"yt-dlp -x -f 'ba' --audio-format m4a -o '~/Downloads/YouTube Videos/50 Anniversary/%(title)s.%(ext)s' {url}")

# url = [
#     'https://youtu.be/TvWotzftWRU',
#     'https://youtu.be/FEvBiayarlc', 
#     'https://youtu.be/FEvBiayarlc',
#     'https://youtu.be/-1J1XqOKnuw',
#     'https://youtu.be/vGxm4vbCyXQ',
#     'https://youtu.be/-IBL3GMzvuw',
#     'https://youtu.be/LzPQXK7KLuA',
#     'https://youtu.be/IA5LEK16xdQ',
#     'https://youtu.be/09wRjwyv1M4',
#     'https://youtu.be/w4qb8JI53F8',
#     'https://youtu.be/ws9K7FkvNvQ',
#     'https://youtu.be/F7j9QehQLe8',
#     'https://youtu.be/ReJ5ZQhu3Bw',
#     'https://youtu.be/qoq8B8ThgEM'
# ]

# start = [
#     '00:00.00',
#     '00:00.00',
#     '01:40.00',
#     '00:00.00',
#     '00:00.00',
#     '00:33.00',
#     '00:00.00',
#     '00:00.00',
#     '00:00.00',
#     '00:00.00',
#     '00:00.00',
#     '00:28.00',
#     '00:12.00',
#     '00:12.00'
# ]

# end = [
#     '00:39.00',
#     '00:16.00',
#     '02:09.00',
#     '01:13.00',
#     '00:49.00',
#     '01:06.00',
#     '01:13.00',
#     '01:15.00',
#     '00:47.00',
#     '01:14.00',
#     '01:09.00',
#     '01:29.00',
#     '00:58.00',
#     '01:06.00'
# ]

# for i in range(len(url)):
#     dl_tp(url[i], start[i], end[i])

dl('https://youtu.be/FEvBiayarlc')
