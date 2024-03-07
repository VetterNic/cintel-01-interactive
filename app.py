import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from shiny.express import ui, input, render

ui.page_opts(title="Nic's PyShiny App with Plot", fillable=True)

with ui.sidebar():
    ui.input_slider("amount_of_bins_chosen", "Nic's Bins", 0, 100, 10)


@render.plot(alt="Nic's Random Histogram")
def histogram():
    count_of_points: int = 537
    np.random.seed(5)
    vetter_random_data_array = 100 + 15 * np.random.randn(count_of_points)
    plt.hist(vetter_random_data_array, input.amount_of_bins_chosen(), density=True)
