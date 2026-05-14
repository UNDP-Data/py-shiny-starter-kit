"""
Example module using sidebar layout to display Iris dataset using basic Shiny functions.
"""

import plotly.express as px
from shiny import module, reactive, render, req, ui
from shinywidgets import output_widget, render_plotly

from ..utils import unsnake

__all__ = ["get_ui", "get_server"]

df_iris = px.data.iris()
variables = sorted(df_iris.filter(regex="sepal|petal").columns)


@module.ui
def get_ui():
    """
    Module function to insert the UI.
    """
    return ui.layout_sidebar(
        ui.sidebar(
            ui.input_selectize(
                "species",
                "Species",
                choices=sorted(df_iris["species"].unique()),
                selected=df_iris["species"].unique().tolist(),
                multiple=True,
            ),
            ui.input_selectize(
                "x",
                "X-axis Variable",
                choices=variables,
                selected=variables[0],
            ),
            ui.input_selectize(
                "y",
                "Y-axis Variable",
                choices=variables,
                selected=variables[1],
            ),
            ui.input_slider(
                "sepal_lengths",
                "Sepal Length Range",
                min=df_iris["sepal_length"].min(),
                max=df_iris["sepal_length"].max(),
                value=(df_iris["sepal_length"].min(), df_iris["sepal_length"].max()),
                step=0.1,
            ),
            title="Sidebar",
        ),
        ui.h3("Example Module"),
        ui.h6("Scatter plot of Iris dataset"),
        output_widget("plot", height="40%", fillable=True),
        ui.h6("Data grid of Iris dataset"),
        ui.output_data_frame("table"),
        height="90vh",
    )


@module.server
def get_server(input, output, session):
    """
    Module function to insert server logic.
    """

    @reactive.calc
    def data():
        """
        Reactive function to filter the data based on the filters.
        """
        return df_iris.query(
            "species in @species and sepal_length.between(@sepal_lengths[0], @sepal_lengths[1])",
            local_dict={
                "species": input.species(),
                "sepal_lengths": input.sepal_lengths(),
            },
        )

    @render_plotly
    def plot():
        """
        Scatter plot function.
        """
        # Ensure the variables are selected to avoid displating an error
        req(input.x(), input.y())
        fig = px.scatter(
            data_frame=data(),
            x=input.x(),
            y=input.y(),
            color="species",
        )
        # Update titles and ensure axes ranges are fixed
        fig.update_layout(
            xaxis={
                "title": unsnake(input.x()),
                "range": [0, df_iris[input.x()].max() * 1.1],
            },
            yaxis={
                "title": unsnake(input.y()),
                "range": [0, df_iris[input.y()].max() * 1.1],
            },
            legend={"title": "Species"},
            dragmode="select",
        )
        fig.update_traces(
            hovertemplate=f"{unsnake(input.x())}: %{{x}}<br>"
            f"{unsnake(input.y())}: %{{y}}"
        )
        return fig

    @render.data_frame
    def table():
        """
        Table display function.
        """
        df = data().rename(unsnake, axis=1)
        return render.DataGrid(df, width="100%", height="100%")
