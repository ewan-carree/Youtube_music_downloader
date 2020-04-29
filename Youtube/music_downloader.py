import youtube_dl
import time
from selenium import webdriver
import subprocess
import os
import sys

#youtube-dl https://youtu.be/zRwt1ER6GkM -x --audio-format "mp3"s

class Youtube():
	"""
	construction du dictionnaire de extract_infos()
	
	['_type', 'entries', 'id', 'title', 'uploader', 'uploader_id', 'uploader_url', 'extractor', 'webpage_url', 'webpage_url_basename', 'extractor_key']

	entries : ['id', 'uploader', 'uploader_id', 'uploader_url', 'channel_id', 'channel_url', 'upload_date', 'license', 'creator', 'title', 'alt_title', 'thumbnail', 'description', 'categories', 'tags', 'subtitles', 'automatic_captions', 'duration', 'age_limit', 'annotations', 'chapters', 'webpage_url', 'view_count', 'like_count', 'dislike_count', 'average_rating', 'formats', 'is_live', 'start_time', 'end_time', 'series', 'season_number', 'episode_number', 'track', 'artist', 'album', 'release_date', 'release_year', 'extractor', 'webpage_url_basename', 'extractor_key', 'n_entries', 'playlist', 'playlist_id', 'playlist_title', 'playlist_uploader', 'playlist_uploader_id', 'playlist_index', 'thumbnails', 'display_id', 'requested_subtitles', 'requested_formats', 'format', 'format_id', 'width', 'height', 'resolution', 'fps', 'vcodec', 'vbr', 'stretched_ratio', 'acodec', 'abr', 'ext']

	"""
	def __init__(self,URL, template_URL):
		self.URL = URL
		self.template_URL = template_URL

	def getInfos(self):
		"""
		Nous souhaitons récupérer l'id, le title et le creator dans des listes
		"""
		infos = {"full_URL" : [], "titre" : [], "auteur" : []}

		extract = youtube_dl.YoutubeDL({}).extract_info(self.URL, download=False)
		for x in range(0,len(extract["entries"])):
			infos["full_URL"].append(self.template_URL + extract["entries"][x]["id"])
			infos["titre"].append(extract["entries"][x]["title"].lower().strip().capitalize())
			infos["auteur"].append(extract["entries"][x]["creator"].lower().strip().capitalize())
		
		return infos

			

	def download():
		pass



