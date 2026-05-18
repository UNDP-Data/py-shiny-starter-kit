"""
Miscellaneous utility functions.
"""

from shiny import ui

__all__ = ["include_markdown", "unsnake"]


def include_markdown(file_path: str) -> ui.HTML:
    """
    Include Markdown from a file.

    Parameters
    ----------
    file_path : str
        Path to a Markdown file file.

    Returns
    -------
    ui.HTML
        Contents from the Markdown file as an ui.HTML tag.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return ui.markdown(file.read())


def unsnake(text: str) -> str:
    """
    Utility function to turn snake case into a title case text.
    """
    return text.replace("_", " ").title()
