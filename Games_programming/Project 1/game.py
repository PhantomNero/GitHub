# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class MyApp(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		self.land = Mapmanager()
		base.camLend.setFov(90)

game = Game()
game.run()