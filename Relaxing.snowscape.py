import random
import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
BGCOLOUR = (100, 100, 255)

SCREEN_WIDTH  = 1824
SCREEN_HEIGHT = 768
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_TITLE  = "<<Snow Scape>>"


class Snowscape:
    """
    attributes:
            coordinates(x,y)
            #Size: how big the snow is(radius
            #Velocity: falling velocity in px/sec

    """
    def __init__(self):

        self.size = 2
        self.coords = [
            (random.randrange(0,SCREEN_WIDTH)),
            (random.randrange(0,SCREEN_HEIGHT))
        ]
        self.y_vel = 4
        self.colour = WHITE

    def update(self) -> None:
        """Updates the Snowscape with every tick"""
        # Update the x-coordinate
        self.x += self.x_vel
        # Update the y-coordinate
        self.y += self.y_vel



def main() -> None:
    """Driver of the Python script"""
    # Create the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(WINDOW_TITLE)

    # Create some local variables that describe the environment
    done = False
    clock = pygame.time.Clock()

    snow = Snowscape

    # ----------- MAIN LOOP
    while not done:
        # ----------- EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------- CHANGE ENVIRONMENT

        # ----------- DRAW THE ENVIRONMENT
        screen.fill(BGCOLOUR)      # fill with bgcolor

        #Draw the snowflake
        pygame.draw.circle(screen, snow.clour, snow.coords, snow.size)

        # Update the screen
        pygame.display.flip()

        # ----------- CLOCK TICK
        clock.tick(75)


if __name__ == "__main__":
    main()