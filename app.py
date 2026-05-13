"""
Application entry point.
"""

from pathlib import Path

from shiny import App, render, ui

from src import components, link_undp_css

theme = ui.Theme.from_brand(__file__)
app_ui = ui.page_fluid(
    ui.head_content(*link_undp_css()),
    components.header(**theme.brand.meta.header),
    ui.br(),
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    components.footer(**theme.brand.meta.footer),
    theme=theme,
)


def server(input, output, session):
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server, static_assets=Path(__file__).parent / "www")
