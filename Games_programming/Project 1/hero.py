key_switch_camera = "x"
key_switch_mode = "z"
key_forward = "w"
key_back = "s"
key_left = "a"
key_right = "d"
key_up = "space"
key_down = "c"
key_turn_left = "l"
key_turn_right = "k"


class Hero:
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel('smiley')  # Загрузка модели героя
        self.hero.setColor(1, 0.5, 0)  # Установка цвета героя
        self.hero.setScale(0.3)  # Установка масштаба героя
        self.hero.setPos(pos)  # Установка позиции героя
        self.hero.reparentTo(render)  # Размещение героя на сцене
        self.cameraBind()  # Привязка камеры
        self.accept_events()  # Регистрация обработчиков событий

    def accept_events(self):
        base.disableMouse()  # Отключение мыши
        base.camera.setH(180)  # Установка горизонтального угла обзора камеры
        base.camera.reparentTo(self.hero)  # Привязка камеры к герою
        base.camera.setPos(0, 0, 1.5)  # Установка позиции камеры
        self.cameraOn = True  # Флаг активации камеры

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def look_at(self, angle):
        x_form = round(self.hero.getX())
        y_form = round(self.hero.getY())
        z_form = round(self.hero.getZ())
        dx, dy = self.check_dir(angle)
        x_to = x_form + dx
        y_to = y_form + dy

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)

    def check_dir(self, angle):
        if 0 <= angle <= 20:
            return 0, -1
        elif angle <= 65:
            return 1, -1
        elif angle <= 110:
            return 1, 0
        elif angle <= 155:
            return 1, 1
        elif angle <= 200:
            return 0, 1
        elif angle <= 245:
            return -1, 1
        elif angle <= 290:
            return -1, 0
        elif angle <= 335:
            return -1, -1
        else:
            return 0, -1

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def accept_events(self):
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right + '-repeat', self.turn_right)
        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)
        base.accept(key_back, self.back)
        base.accept(key_back + '-repeat', self.back)
        base.accept(key_left, self.left)
        base.accept(key_left + '-repeat', self.left)
        base.accept(key_right, self.right)
        base.accept(key_right + '-repeat', self.right)
        base.accept(key_switch_camera, self.changeView)