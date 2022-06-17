
### third-party imports

## pygame

from pygame import (
              KEYUP, K_ESCAPE,
            )

from pygame.display import get_surface, update

from pygame.time import Clock

from pygame.event import get as get_events

from pygame.image import fromstring


## matplotlib
from matplotlib.figure import Figure



SCREEN      = get_surface()
SCREEN_RECT = SCREEN.get_rect()

CLOCK = Clock()

MODE = 'RGB'

def view_figure(figure:Figure):

    canvas = figure.canvas
    canvas.draw()

    raw_data = canvas.tostring_rgb()
    size     = canvas.get_width_height()

    figure_surf = fromstring(
                    raw_data,
                    size,
                    MODE,
                  )

    figure_rect = figure_surf.get_rect()
    figure_rect.center = SCREEN_RECT.center

    SCREEN.fill((128, 128, 128))
    SCREEN.blit(figure_surf, figure_rect)

    running = True

    while running:
        
        CLOCK.tick(30)
        
        for event in get_events():
            
            if (
                  event.type == KEYUP
              and event.key  == K_ESCAPE
            ):
                running = False

        update()

view_figure.dismiss_exec_time_tracking = True

main_callable = view_figure
