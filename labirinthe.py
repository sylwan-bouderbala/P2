class Lab(object):
	def __init__(self,reglage,size=15):
		self.format={}
		self.reglage=reglage
		self.size=size
	def initialisermap(self):
		positions=[]
		for i in range(size):
			for j in range(size):
				positions.append((i,j))

		file=self.reglage.read()
		liste2=[]
		for caracters in file:
			if caracters != "\n":
			    liste2.append()
			else :
				pass 
		for x in range(size*size):
			self.format[positions[x]]=liste2[x]
	def affichermap(self):
		

			


