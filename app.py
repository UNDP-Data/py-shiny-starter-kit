"""
Application entry point.
"""

from pathlib import Path

from shiny import App, reactive, ui
from undp_brand_yml.plotting import set_plotly_theme

from src import components, link_undp_css, link_undp_js, modules, include_markdown

set_plotly_theme()
theme = ui.Theme.from_brand(__file__)
app_ui = ui.page_fluid(
    ui.head_content(*link_undp_css(), *link_undp_js()),
    components.header(
        **theme.brand.meta.header,
        navs=[
            {"text": "Example Module", "value": "page1"},
            {"text": "About", "value": "page2"},
        ],
    ),
    ui.navset_hidden(
        ui.nav_panel(None, modules.example.get_ui("page1"), value="page1"),
        ui.nav_panel(
            None,
            ui.div(
                include_markdown("www/mk/about.md"),
                class_="p-5 vh-100",
            ),
            value="page2",
        ),
        id="pages",
    ),
    components.footer(**theme.brand.meta.footer),
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

    modules.example.get_server("page1")


app = App(app_ui, server, static_assets=Path(__file__).parent / "www")
