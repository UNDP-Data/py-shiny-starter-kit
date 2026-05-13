"""
Custom components based on the UNDP Design System (https://design.undp.org).
"""

from typing import Literal, NotRequired, TypedDict

from shiny import ui

from .utils import include_html

__all__ = ["header", "footer"]


class Anchor(TypedDict):
    """
    Anchor tag details.
    """

    text: str
    href: NotRequired[str]


def header(
    region: str | Anchor, title: str | Anchor, logo: Literal["undp", "pnud"] = "undp"
) -> ui.HTML:
    """
    Add an HTML component for UNDP country header.

    See https://design.undp.org/?path=/docs/components-navigation-components-main-navigation-country-site-header--docs.

    Parameters
    ----------
    region : str or Anchor
        Region/unit details displayed next to the logo.
    title : str
        Website title details displated below the region name.
    logo : {'undp', 'pnud'}, default='undp'
        Type of the official logo to use.
    """
    return include_html(
        "www/html/header.html",
        region=region if isinstance(region, dict) else {"text": region},
        title=title if isinstance(title, dict) else {"text": title},
        logo=f"images/{logo}-logo-blue.svg",
    )


def footer(logo: Literal["undp", "pnud"] = "undp") -> ui.HTML:
    """
    Add an HTML component for UNDP footer.

    See https://design.undp.org/?path=/docs/components-ui-components-footer--docs.

    Parameters
    ----------
    logo : {'undp', 'pnud'}, default='undp'
        Type of the official logo to use.
    """
    return include_html("www/html/footer.html", logo=f"images/{logo}-logo-white.svg")
