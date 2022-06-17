
### third-party import

from matplotlib.pyplot import subplots
from matplotlib.figure import Figure

def create_pie(**data) -> [{'name': 'figure', 'type': Figure}]:

    labels, values = zip(*data.items())

    figure, axis = subplots()

    axis.pie(
           values,
           labels=[label.title() for label in labels],
         )

    return figure

main_callable = create_pie
