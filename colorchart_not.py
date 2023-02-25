import pygame
import random
import csv
from sklearn.neighbors import KNeighborsClassifier

with open("pretty_yes.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    pretty_yes = [list(map(int, r)) for r in reader if r != [] and r[0] != "R"]

with open("pretty_no.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    pretty_no = [list(map(int, r)) for r in reader if r != [] and r[0] != "R"]

color_data = pretty_yes + pretty_no
color_target = [1] * len(pretty_yes) + [0] * len(pretty_no)

kn = KNeighborsClassifier(n_neighbors=5)
kn.fit(color_data, color_target)

class EachColor(pygame.sprite.Sprite):
    def __init__(self, top, left, width, height):
        super().__init__()
        self.color = self.colorselect()
        pygame.draw.rect(screen, self.color, (top, left, width, height))

    def colorselect(self):
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        while kn.predict([color]) == [1]:
            color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        return color

def main():
    for i in range(0, width, side):
        for j in range(0, height, side):
            randcolor = EachColor(i, j, side, side)
            all_sprites.add(randcolor)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    width = 400
    height = 400
    side = 16
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("not pretty")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    main()