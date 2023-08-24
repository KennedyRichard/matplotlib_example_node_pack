
### third-party imports

## pygame-ce

from pygame import Surface

from pygame.image import frombytes


## matplotlib

from matplotlib.figure import Figure

from matplotlib.pyplot import close



### main callable

def surface_from_figure(

    figure:Figure,
    close_figure: bool = True,

) -> [

    {'name': 'surface', 'type': Surface},

]:
    """Return dict with pygame-ce Surfaces created from given figure.

    Parameters
    ==========

    figure
        Matplotlib figure to be converted into pygame.Surface(s).
    close_figure
        If True (default), the figure is closed after it is converted
        into a surface.
    """
    ### convert figure to pygame-ce surface; this is the surface
    ### representing the full-size figure

    canvas = figure.canvas
    canvas.draw()

    raw_data = canvas.tostring_rgb()
    size     = canvas.get_width_height()

    surface = frombytes(

                  raw_data,
                  size,

                  # image mode
                  'RGB',

                )

    ### if requested, close the figure
    if close_figure:
        close(figure)

    ### finally, return the surface
    return surface


### alias surface_from_figure as the main callable
main_callable = surface_from_figure

