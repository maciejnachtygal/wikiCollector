import os

#
# Funkcja do otwierania plikow - tylko READ
#
def openFile(fileName, mode):
	# Sprawdz czy plik istnieje
	try:
		# Wczytaj plik 
		file = open(os.path.join(os.path.dirname(__file__), fileName), mode)
		# content = file.read(100)
		# Komunikat
		print("Plik " + fileName + " zostal wczytany poprawnie!")
		#print(content)
		return file

	# Plik nie zostal odnaleziony
	except FileNotFoundError:
		# Komunikat o bledzie
		print("Ups! Chyba cos poszlo nie tak... Sprobuj ponownie.")

#
# Funkcja do tworzenia plikow
#
def createFile(fileName, mode):
	#	Sprawdz czy plik istnieje
	try:
		#	Utworz plik 
		file = open(os.path.join(os.path.dirname(__file__), fileName), mode)
		#content = file.read(100)
		#	Komunikat
		print("Plik " + fileName + " zostal utworzony poprawnie!")
		#print(content)
		return file

	#	Plik nie zostal odnaleziony
	except FileNotFoundError:
		#	Komunikat o bledzie
		print("Ups! Chyba cos poszlo nie tak... Sprobuj ponownie.")

#  KICAD:      Ref,Val,Package,PosX,PosY,Rot,Side
#  HCT:        Type,Package,X,Y,Nozzle,Feeder,,,,Angle,

#
# Klasa danych z kiCADa
#
class kicadDataStructure(object):

	def __init__(self, ref, val, package, x, y, angle, side):
		self.ref = ref
		self.val = val
		self.package = package
		self.x = x
		self.y = y
		self.angle = angle
		self.side = side