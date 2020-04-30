import music_downloader as msd
import lib
import sys

# Etape 1 : vérifier l'OS
# Etape 2 : définir le path de téléchargement
# Etape 3 : extraire l'URL de la playlist passé en argument 
# Etape 4 : extraire les informations sur chaque musique
# Etape 5 : télécharger la playlist
# Etape 6 : renommer chaque fichier (artistName - musicName)

def main():
	# Etape 1
	lib.detect_OS()
	# Etape 2 et 3
	playlistURL = lib.extract_args("C:/Users/carre/Music")
	Youtube = msd.Youtube(playlistURL,"https://www.youtube.com/watch?v=")
	# Etape 4
	infos = Youtube.getInfos()
	# Etape 5
	Youtube.download(infos)
	# Etape 6


if __name__ == '__main__':
	main()
