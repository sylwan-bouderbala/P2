import os

import labirinthe


class Perso(object):
	def __init__(self):
		self.position=()

	def ids(self,tab):
		for i,v in tab.items():
			if v==1:
				self.position=i
				self.id=1
			if v==2:
				self.position=i
				self.id=2
