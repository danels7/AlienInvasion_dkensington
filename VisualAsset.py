from pygame import Surface


class VisualAsset:
    def __init__(self, parentScreen: Surface, img: Surface):
        self.img = img.copy()
        self.rect = img.get_rect()
        self.parent = parentScreen

    def draw(self) -> None:
        self.parent.blit(self.img, self.rect)