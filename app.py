
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render


ui.page_opts(title="Mahesh Bashyal's PyShiny Plot", fillable=True)
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "number of bins", 0, 100, 20)


@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    count_of_points: int = 437
    np.random.seed(3000)

    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)
