import youtube_dl
import subprocess
import os
import sys

#youtube-dl https://youtu.be/zRwt1ER6GkM -x --audio-format "mp3"

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
		infos = {"full_URL" : [], "titre" : [], "auteur" : [], "notCorresponding": []}

		ydlOpts = {'ignoreerrors': 'true'}
		youtube_dl.YoutubeDL(ydlOpts).cache.remove()
		extract = youtube_dl.YoutubeDL(ydlOpts).extract_info(self.URL, download=False)
		
		for x in range(0,len(extract["entries"])):
			if extract["entries"][x] != None:
				if "Music" in extract["entries"][x]["categories"]:
					infos["full_URL"].append(self.template_URL + extract["entries"][x]["id"])
					infos["auteur"].append(extract["entries"][x]["creator"])
					infos["titre"].append(extract["entries"][x]["title"])

				if "Music" not in extract["entries"][x]["categories"]:
					infos["notCorresponding"].append(extract["entries"][x]["title"])
			else:
				print("At least one content is blocked by Youtube")
				
		if len(infos["notCorresponding"])!=0:
			print("Part of the playlist isn't corresponding to the good format")
			print(infos["notCorresponding"])


		return infos

			

	def download(self,infos,names_file):
		i=0
		for url in infos["full_URL"]:
			try:
				os.system('youtube-dl {} -x --audio-format "mp3" -o "{}.%(ext)s"'.format(url, names_file[i]))
			except Exception:
				print("le fichier {} n'a pas pu être téléchargé".format(names_file[i]))
			i+=1


	def sortName(self,dico):
		names_file = []

		infos = dico["titre"]

		for titre in infos:
			if '(' in titre:
				position_dans_liste = infos.index(titre)
				position_dans_titre = titre.index('(')
				if ')'in titre:
					position_dans_liste2 = infos.index(titre)
					position_dans_titre2 = titre.index(')')					
					infos[position_dans_liste] = infos[position_dans_liste][:position_dans_titre].strip()+infos[position_dans_liste2][position_dans_titre2+1:]
			if '[' in titre:
				position_dans_liste = infos.index(titre)
				position_dans_titre = titre.index('[')
				if ']'in titre:
					position_dans_liste2 = infos.index(titre)
					position_dans_titre2 = titre.index(']')					
					infos[position_dans_liste] = infos[position_dans_liste][:position_dans_titre].strip()+infos[position_dans_liste2][position_dans_titre2+1:]
		for titre in infos:
			if '(' in titre:
				position_dans_liste = infos.index(titre)
				position_dans_titre = titre.index('(')
				if ')'in titre:
					position_dans_liste2 = infos.index(titre)
					position_dans_titre2 = titre.index(')')					
					infos[position_dans_liste] = infos[position_dans_liste][:position_dans_titre].strip()+infos[position_dans_liste2][position_dans_titre2+1:]
			if '[' in titre:
				position_dans_liste = infos.index(titre)
				position_dans_titre = titre.index('[')
				if ']'in titre:
					position_dans_liste2 = infos.index(titre)
					position_dans_titre2 = titre.index(']')					
					infos[position_dans_liste] = infos[position_dans_liste][:position_dans_titre].strip()+infos[position_dans_liste2][position_dans_titre2+1:]
		
		i=0
		for elem in dico["auteur"]:
			if elem != None:
				if str(elem) in str(infos[i]):
					name_file = str(infos[i]).capitalize()
					names_file.append(name_file)
				else:
					name_file = str(elem).capitalize() + ' - ' + str(infos[i]).capitalize()
					names_file.append(name_file)
			else:
				name_file = str(infos[i]).capitalize()
				names_file.append(name_file)
			i+=1
				
		return names_file
