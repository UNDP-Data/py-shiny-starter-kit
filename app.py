"""
Application entry point.
"""

from pathlib import Path

from shiny import App, reactive, ui
from undp_brand_yml.plotting import set_plotly_theme
from undp_design_system import footer, header, render_footer, render_header

from src import modules, include_markdown

set_plotly_theme()
theme = ui.Theme.from_brand(__file__)
app_ui = ui.page_fluid(
    header("header"),
    ui.navset_hidden(
        ui.nav_panel(None, modules.example.get_ui("page1"), value="page1"),
        ui.nav_panel(
            None,
            ui.div(include_markdown("www/about.md"), class_="p-5 vh-100"),
            value="page2",
        ),
        id="pages",
    ),
    footer("footer"),
    theme=theme,
)


def server(input, output, session):

    @reactive.effect
    @reactive.event(input.page_switch)
    def switch_page():
        """
        Reactive function to switch pages from the header.
        """
        ui.update_navset("pages", selected=input.page_switch())

    @render_header()
    def header():
        """
        Function to render the header. You can use it to customise the header based on app inputs if necessary.
        """
        return theme.brand.meta.header | {
            "navs": [
                {"text": "Example", "value": "page1"},
                {"text": "About", "value": "page2"},
            ],
        }

    @render_footer
    def footer():
        """
        Function to render the footer.
        """
        return theme.brand.meta.footer

    modules.example.get_server("page1")


app = App(app_ui, server, static_assets=Path(__file__).parent / "www")
