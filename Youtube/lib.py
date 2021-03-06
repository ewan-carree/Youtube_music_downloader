import platform
import sys
import os

def detect_OS():
	OS = platform.system()
	if OS == "Linux":
		print("This program isn't built for Linux system")
		sys.exit(0) 

def extract_args(path):
	"""
	Cette fonction permet de récupérer les arguments passés lors de l'appel du programme. 
	Si l'utilisateur veut créer un fichier, on se place dans le dossier musique et on le créer puis on va dedans.
	Sinon on se place juste dans le dossier musique

	"""
	arguments = sys.argv
	assert isinstance(arguments, list)
	arguments = arguments[1:]
	if len(arguments) < 1 :
		print("Vous n'avez pas passé le bon nombre d'argument(s), veuillez les saisir à nouveau.")
		sys.exit(0)

	set_path(path) #va dans le dossier musique

	if len(arguments)>=2:
		#recupérer le reste de la ligne pour le nom du fichier
		folder = arguments[1:]
		folder = ' '.join(folder).strip()
		create_file(folder) #créer le dossier
		set_path(path+'/'+folder) #va dans le nouveau dossier de musique

	return arguments[0]

def renameFile(infos):
	pass

create_file = lambda fileName : os.mkdir(fileName) #créer le dossier de travail

get_path = lambda : os.getcwd() #répertoire actuel

set_path = lambda fileName : os.chdir(fileName) #va dans le dossier de travail
