
### third-party imports

from matplotlib.pyplot import subplots, get_fignums, close

from matplotlib.figure import Figure



### main callable

def create_pie(

    max_live_figures: 'positive_integer' = 20,

    **data,

) -> [{'name': 'figure', 'type': Figure}]:
    """Return figure representing a pie chart.

    Parameters
    ==========

    max_live_figures
        Since matplotlib keeps a lot of state, we need to free some
        memory manually in order to avoid using too much.

        Each call to this function adds a figure in the memory,
        which is kept internally by matplotlib.

        During the call, before creating the figure, we check whether
        creating the new figure would cause the number of opened (live)
        figures to exceed "max_live_figures" and, if that would be the
        case, we close the oldest one(s) that would exist in excess
        after creating the one returned by this function.

    **data
        label/quantity pairs to use in the pie chart.
    """
    ### ensure max_live_figures is an integer >= 1

    if not isinstance(max_live_figures, int):
        raise TypeError("'max_live_figures' must an integer")

    elif max_live_figures < 1:
        raise ValueError("'max_live_figures' must be >= 1")

    ### ensure number of max live figures won't be exceeded

    live_figure_indices = get_fignums()
    n_alive = len(live_figure_indices)

    if n_alive + 1 > max_live_figures:

        excess_amount = n_alive + 1 - max_live_figures

        for exceeding_figure_index in live_figure_indices[:excess_amount]:
            close(exceeding_figure_index)

    ### create and return figure

    labels, values = zip(*data.items())

    figure, axis = subplots()

    axis.pie(
           values,
           labels=[label.title() for label in labels],
         )

    return figure

### alias create_pie as main_callable
main_callable = create_pie
