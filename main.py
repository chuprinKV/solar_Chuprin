import pygame
from pygame import *
from flyobj import *

WIN_WIDTH = 1280
WIN_HEIGHT = 720
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
PLANET_WIDTH = 20
PLANET_HEIGHT = 20
SPACE_COLOR = "#000022"
SUN_COLOR = "#ffcf48"
PLANET_COLOR = "#87CEEB"
# Условие остановки
CRASH_DIST = 10
OUT_DIST = 1000

def main():
    # PyGame init
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Solar")

    # Space init
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(SPACE_COLOR))
    draw.circle(bg, Color(SUN_COLOR), (X0, Y0), 20)

    # Timer init
    timer = pygame.time.Clock()

    # Unknown Planet init
    planet = Surface((PLANET_WIDTH, PLANET_HEIGHT))
    planet.fill(Color(SPACE_COLOR))
    draw.circle(planet,
                Color(PLANET_COLOR),
                (PLANET_WIDTH // 2, PLANET_HEIGHT // 2),
                5)

    unknown_planet_1 = FlyObject(
                    int(1.0),
                    float(1180.0),
                    float(290.0),
                    float(0.1),
                    float(1.5)
                    )
    unknown_planet_2 = FlyObject(
        int(1.0),
        float(100.0),
        float(290.0),
        float(0.1),
        float(1.5)
    )

    done = False
    while not done:
        timer.tick(50)
        for e in pygame.event.get():
            if e.type == QUIT:
                done = True
                break

        r = unknown_planet_1.calc()
        r = unknown_planet_2.calc()

        screen.blit(bg, (0, 0))
        screen.blit(planet, (int(unknown_planet_1.x), int(unknown_planet_1.y)))
        screen.blit(planet, (int(unknown_planet_2.x), int(unknown_planet_2.y)))
        pygame.display.update()

        if r < CRASH_DIST:
            done = True
            print("Crashed")
            break
        if r > OUT_DIST:
            done = True
            print("Out of system")
            break

if __name__ == "__main__":
    main()