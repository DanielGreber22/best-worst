import pygame
import time 
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("happy card")

img = pygame.image.load("5.jpg")
image = pygame.transform.scale(img,(600,600))

img2 = pygame.image.load("6.png")
image2 = pygame.transform.scale(img2,(600,600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    font = pygame.font.SysFont("Arial",60)
    text = font.render("best guy",True,"purple")
    screen.blit(image,(0,0))
    screen.blit(text,(40,200))
    pygame.display.update()
    time.sleep(2)

    font = pygame.font.SysFont("Arial",60)
    text2 = font.render("Have a BAD second",True,"purple")
    screen.blit(image2,(0,0))
    screen.blit(text2,(40,200))
    pygame.display.update()
    time.sleep(2)


pygame.quit()