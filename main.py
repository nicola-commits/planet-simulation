import time
from body import Body
import pygame
import math
from bodycreator import Creator

earthdistance = 150000000000
earthradius = 6371000
earthmass = 6 * (10 ** 24)

sunradius = 700000000
sunmass = 2 * (10 ** 30)

body1 = Body(earthdistance, 0, earthmass, earthradius, 1, speed=[0, 0.7], color=(0, 0, 255))  # earth
body2 = Body(0, 0, sunmass, sunradius, 2, [0, 0], (0, 255, 255))  # sun

bodylist = [body1, body2]

# pygame stuff
screensize = (1080, 800)

pygame.init()
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("planetSimulation")

font = pygame.font.SysFont('Arial', 13)
text = font.render('0', True, (0, 0, 255))
textRect = text.get_rect()

#creator
c = Creator()
# c.show()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.fill((0, 0, 0))

    for body in bodylist:
        forces = body.update(bodylist)
        drawnx = (body.x / earthdistance * 200 + (screensize[0] / 2))
        drawny = (body.y / earthdistance * 200 + (screensize[1] / 2))
        drawnsize = math.log10(body.radius)
        pygame.draw.circle(screen, body.color, [drawnx, drawny], drawnsize)
        # text
        font = pygame.font.SysFont('Arial', 12)

        mass_text = 'M={:.2e}'.format(body.mass)
        force_text = f'F=({forces[0].__round__(2)},{forces[1].__round__(2)})'
        velocity_text = f'V=({body.speed[0].__round__(1)},{body.speed[1].__round__(1)})'
        text_str = mass_text + ' ' + force_text + ' ' + velocity_text

        text = font.render(text_str, True, (0, 0, 255))
        textRect.center = (drawnx, drawny + 20)
        screen.blit(text, textRect)

    pygame.display.flip()

    time.sleep(0.05)
