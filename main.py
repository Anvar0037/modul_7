import pygame

pygame.init()
pygame.display.set_caption("Killer bmw")

screen = pygame.display.set_mode((600, 700), pygame.RESIZABLE)

icon = pygame.image.load("C:\\Users\Victus\\PycharmProjects\\modul_7\\img_2.png")
pygame.display.set_icon(icon)

white = pygame.Color('#FFFF00')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(color=white)
        pygame.display.update()



pygame.quit()
