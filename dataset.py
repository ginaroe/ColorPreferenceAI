import pygame
import random
import csv
from rgb_hsv import rgb_to_hsv

class EachColor(pygame.sprite.Sprite):
    def __init__(self, border, width, height):
        super().__init__()
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pygame.draw.rect(screen, self.color, (border, border, width - border * 2, height - border * 2))

    def update(self):
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pygame.draw.rect(screen, self.color, (border, border, width - border * 2, height - border * 2))

def main():
    randcolor = EachColor(border, width, height)
    all_sprites.add(randcolor)
    count = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dataset.add((randcolor.color, 1))
                elif event.key == pygame.K_RIGHT:
                    dataset.add((randcolor.color, 0))
                all_sprites.update()
                count += 1
                print(count)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    return dataset


if __name__ == "__main__":
    pygame.init()
    width = 200
    height = 200
    border = 20
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("original")
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    dataset = set()
    dataset = main()

    pretty_yes = [i for i,j in dataset if j==1]
    pretty_no = [i for i,j in dataset if j==0]
    print(len(pretty_yes), len(pretty_no))

    with open("pretty_yes.csv", "a", encoding="utf-8") as f:
        wr = csv.writer(f)
        for color in pretty_yes:
            wr.writerow(color)

    with open("pretty_no.csv", "a", encoding="utf-8") as f:
        wr = csv.writer(f)
        for color in pretty_no:
            wr.writerow(color)

    pretty_yes_hsv = [rgb_to_hsv(r, g, b) for r, g, b in pretty_yes]
    pretty_no_hsv = [rgb_to_hsv(r, g, b) for r, g, b in pretty_no]

    with open("pretty_yes_hsv.csv", "a", encoding="utf-8") as f:
        wr = csv.writer(f)
        for color in pretty_yes_hsv:
            wr.writerow(color)

    with open("pretty_no_hsv.csv", "a", encoding="utf-8") as f:
        wr = csv.writer(f)
        for color in pretty_no_hsv:
            wr.writerow(color)

    print("Done")