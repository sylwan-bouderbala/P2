import os 

class Lab(object):
	def __init__(self, size=15):
		self.size = size
		self.format={}
	def init(self,size=15):
		liste2=[]
		liste3=[]
		with open('lab.txt','r') as filereglage:
				liste2=filereglage.read()
				for i in liste2:
					if i != "\n":
						liste3.append(i)
					else :
						pass

		listeplace=[]
		for i in range(15):
			for j in range(15):
				listeplace.append((i,j))

		for i in range(15**2):
			self.format[listeplace[i]]=liste3[i]
	def affichage(self):
		listeaffichage=""
		for i in range(15):
			for j in range(16):
				if j != 15  :
				  listeaffichage= listeaffichage+self.format[(i,j)]+" "
				else:
					listeaffichage=listeaffichage + "\n"
		print listeaffichage
		
		
tab= Lab()
tab.init()
tab.affichage()
