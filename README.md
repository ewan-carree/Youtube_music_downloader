# Youtube_music_downloader
Download a whole playlist from youtube into mp3 files directly in your Music directory with or without a special folder. Usefull to download albums' artists

NOT EXECUTABLE SINCE COUPLE DAYS, YOUTUBE-DL CHANGED !!!!!!!!

## Prerequisite
download youtube-dl 

download ffmpg (https://www.youtube.com/watch?v=qjtmgCb8NcE)

## Errors handling
Some errors may occure : ERROR: unable to download video data: HTTP Error 403: Forbidden

Fix it by writing "youtube-dl --rm-cache-dir" in the console

Problem now fixed but I leave this comment to remember in case of need.

ERROR: No video formats found; please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output.

PROBLEM !!!!!

## Use
python3 pathTofile\main.py URL Folder

Folder argument is optionnal, if you put it, it will download content directly into this folder. Else it will download into music directory on youre computer

## Tip
Edit the file ~/.bash_aliases this way : alias youtube='python3 /mnt/c/Users/carre/Desktop/Workspace_ubuntu/Projets_perso/Youtube_music_downloader/main.py'

It will be much more easier to use this program, now you can run it with : youtube URL Folder

## For futher
https://www.programcreek.com/python/example/98358/youtube_dl.YoutubeDL  Usefull webpage with clear exemples
