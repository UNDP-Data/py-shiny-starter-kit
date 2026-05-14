"""
Miscellaneous utility functions.
"""

from jinja2 import Template
from shiny import ui

__all__ = ["include_html", "link_undp_css", "link_undp_js", "unsnake"]


CDN_URL = "https://cdn.jsdelivr.net/npm/@undp/design-system-assets"


def include_html(file_path: str, **kwargs) -> ui.HTML:
    """
    Include HTML from a file.

    Parameters
    ----------
    file_path : str
        Path to an HTML file.
    **kwargs
        Extra variables to pass to the Jinja2 template for rendering.

    Returns
    -------
    ui.HTML
        Contents from the file as an ui.HTML tag.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        template = Template(file.read()).render(**kwargs)
    return ui.HTML(template)


def link_undp_css() -> list[ui.Tag]:
    """
    Link the official stylesheets from the UNDP Design System.

    See https://design.undp.org/?path=/docs/getting-started-how-to-use-our-design-system--docs
    for detailed information on the design system.

    Returns
    -------
    list[ui.Tag]
        Link tags to be inserted into the page head.
    """
    return [
        ui.tags.link(rel="stylesheet", href=f"{CDN_URL}/css/{href}")
        for href in (
            "base-minimal.min.css",
            "components/country-site-header.min.css",
            "components/menu.min.css",
            "components/mobile-nav.min.css",
            "components/footer.min.css",
        )
    ]


def link_undp_js() -> list[ui.Tag]:
    """
    Link the official JS scripts from the UNDP Design System.

    See https://design.undp.org/?path=/docs/getting-started-how-to-use-our-design-system--docs
    for detailed information on the design system.

    Returns
    -------
    list[ui.Tag]
        Script tags to be inserted into the page head.
    """
    return [
        ui.tags.script(src=f"{CDN_URL}/js/{href}")
        for href in ("init.js", "navigation.min.js")
    ]


def unsnake(text: str) -> str:
    """
    Utility function to turn snake case into a title case text.
    """
    return text.replace("_", " ").title()
