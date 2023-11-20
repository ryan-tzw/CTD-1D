class Camera:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y
