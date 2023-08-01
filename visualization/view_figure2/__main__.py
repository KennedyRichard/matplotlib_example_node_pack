
### third-party imports

## pygame-ce

from pygame import Surface

from pygame.math import Vector2

from pygame.image import frombytes

from pygame.transform import smoothscale as smoothscale_surface


## matplotlib
from matplotlib.figure import Figure



### get vector representing the origin
ORIGIN = Vector2()


### main callable

def view_figure2(

    figure:Figure,
    max_preview_size: 'natural_number' = 0,

) -> [

    {'name': 'full_surface', 'type': Surface, 'viz': 'loop'},
    {'name': 'preview_surface', 'type': Surface, 'viz': 'side'},

]:
    """Return dict with pygame-ce Surfaces created from given figure.

    Parameters
    ==========

    figure
        Matplotlib figure to be converted into pygame.Surface(s).
    max_preview_size
        Maximum value in pixels of diagonal length. If 0, the preview
        is the same size of the figure.
    """

    ### raise error if value of max preview size is not allowed

    if max_preview_size < 0:
        raise ValueError("'max_preview_size' must be >= 0")

    ### convert figure to pygame-ce surface; this is the surface
    ### representing the full-size figure

    canvas = figure.canvas
    canvas.draw()

    raw_data = canvas.tostring_rgb()
    size     = canvas.get_width_height()

    full_surf = frombytes(

                  raw_data,
                  size,

                  # image mode
                  'RGB',

                )

    ### if max preview size is 0, use the full surface as the preview
    ### and return the surfaces from here

    if not max_preview_size:

        return {
            'full_surface': full_surf,
            'preview_surface': full_surf,
        }


    ### otherwise, create preview surface (if needed)

    ## obtain bottomright coordinate of full-size surface, which is equivalent
    ## to its size
    bottomright = full_surf.get_size()

    ## if the diagonal length of the full-size surface is longer than
    ## the maximum size allowed for the preview, create a smaller surface
    ## for the preview

    diagonal_length = ORIGIN.distance_to(bottomright)

    if diagonal_length > max_preview_size:

        size_proportion = max_preview_size / diagonal_length
        new_size = ORIGIN.lerp(bottomright, size_proportion)

        preview_surf = smoothscale_surface(full_surf, new_size)

    ## otherwise it means the full surface is equal or smaller than the
    ## allowed size, so we can use it as the preview surface itself

    else:
        preview_surf = full_surf

    ### return surfaces

    return {
        'full_surface': full_surf,
        'preview_surface': preview_surf,
    }


### alias view_figure2 as the main callable
main_callable = view_figure2

