# напиши здесь код создания и управления картой
class Mapmanager():
    def __init__(self):
        self.model = "block"
        self.texture = "block.png"
        self.color = (0.2, 0.2, 0.35, 1)
        # Основной узел карты.
        self.startNew()
        self.addBlock((0, 10, 0))

    def startNew(self):
        self.land = render.attachNewMode("Land")

    def addBlock(self, possition):
        self.block = self.loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        set.block.setColor(self.color)
        self.block.reparentTo(self.land)

