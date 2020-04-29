import music_downloader as msd
import lib
import sys

# Etape 1 : extraire l'URL de la playlist passé en argument
# Etape 2 : définir le path de téléchargement
# Etape 3 : extraire les informations sur chaque musique
# Etape 4 : télécharger la playlist
# Etape 5 : renommer chaque fichier (artistName - musicName)

template_URL = "https://www.youtube.com/watch?v="
URL = "https://www.youtube.com/playlist?list=PLbwBenSp6mG0zJGx8b6dMxVwkqul8b84P" 

def main():
	"""OS = lib.detect_OS()
	if OS == "Linux":
		print("This program isn't built for Linux system")
		sys.exit(0)
	playlistURL = lib.extract_args("C:/Users/carre/Music")"""


	#Youtube = msd.Youtube(URL,template_URL)
	#infos = Youtube.getInfos()
	#print(infos)

if __name__ == '__main__':
	main()