# Youtube_music_downloader
Download a whole playlist from youtube into mp3 files directly in your Music directory with or without a special folder. Usefull to download albums' artists

Prérequis : installer youtube-dl 
            installer ffmpg (https://www.youtube.com/watch?v=qjtmgCb8NcE)

Some errors may occure : ERROR: unable to download video data: HTTP Error 403: Forbidden
Fix it by writing "youtube-dl --rm-cache-dir" in the console

Problem now fixed but I leave this comment to remember in case of need.

Use : python pathTofile\main.py URL Folder
folder argument is optionnal, if you put it, it will download content directly into this folder. Else it will download into music directory on youre computer


https://www.programcreek.com/python/example/98358/youtube_dl.YoutubeDL  Usefull webpage with clear exemples
