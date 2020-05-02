import music_downloader as msd
import lib
import sys

# Etape 1 : vérifier l'OS
# Etape 2 : définir le path de téléchargement
# Etape 3 : extraire l'URL de la playlist passé en argument 
# Etape 4 : extraire les informations sur chaque musique
# Etape 5 : renommer chaque fichier (artistName - musicName)
# Etape 6 : télécharger la playlist

template_URL = "https://www.youtube.com/watch?v="
URL = "https://www.youtube.com/playlist?list=PLbwBenSp6mG0zJGx8b6dMxVwkqul8b84P" #a enlever plus tard et remplacer par playlistURL

def main():
	lib.detect_OS()
	playlistURL = lib.extract_args("C:/Users/carre/Music")
	Youtube = msd.Youtube(playlistURL,template_URL)
	infos = Youtube.getInfos()
	names_file = Youtube.sortName(infos)
	Youtube.download(infos,names_file)


if __name__ == '__main__':
	main()
