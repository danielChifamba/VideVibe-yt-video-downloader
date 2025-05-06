import yt_dlp
import os

MEDIA_PATH = 'Downloads'

def getDetails(url):
    ydl_opts = {
        'noplaylist': False,
        'quiet': True,
        'skip_download': True,
    }

    vidInfo = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # extract vid info
        video_info = ydl.extract_info(url, download=False)
        # ydl.download([url])

        # extract details
        videoTitle = video_info.get('title', 'No Title Available')
        videoDescription = video_info.get('description', 'No Description Available')
        videoThumbnail = video_info.get('thumbnail', 'No Thumbnail Available')
        videoURL = url

        # downloadLink = ''
        # if 'url' in video_info:
        #     downloadLink = video_info['url']

        # elif 'formats' in video_info:
        #     for format in video_info['formats']:
        #         if format['ext'] == 'm3u8':
        #             continue
        #         if format['vcodec'] != 'none' and format['codec'] != 'none':
        #             downloadLink = format['url']
        #             break
        
        # else:
        #     downloadLink = 'Failed to generate link...'

        vidInfo = {
            'url': videoURL,
            'title': videoTitle,
            'description': videoDescription,
            'thumbnailURL': videoThumbnail,
        }

    return vidInfo

def downloadMedia(url, format_type, title):
    ext = 'mp4' if format_type == 'video' else 'mp3'
    filename = f"VideVibe - {title}.{ext}"
    filepath = os.path.join(MEDIA_PATH, filename)

    ytdl_opts = {
        'outtmpl': filepath,
        'format': 'bestvideo+bestaudio' if format_type == 'video' else 'bestaudio/best',
        'merge_output_format': ext,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3' if format_type == 'audio' else 'mp4',
            'preferredquality': '192'
        }] if format_type == 'audio' else [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }]
    }

    with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
        # info = ydl.extract_info(url)
        # file_final = filepath + f'.{ext}'
        # os.rename(ydl.prepare_filename(info), file_final)
        ydl.download([url])

    return filepath

def truncateWords(description, max_length=250):
    if len(description) > max_length:
        return description[:max_length] + " ..."
    return description