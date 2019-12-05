import os

import labirinthe


class Perso(object):
	def __init__(self):
		self.position=()
	def positionner(self,tag,tab):
		for i,v in tab.items():
			if v==tag:
				self.position=(i)

