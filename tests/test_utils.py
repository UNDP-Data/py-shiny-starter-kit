"""
Unit tests for the utility module.
"""

from typing import Any

import pytest
from jinja2.exceptions import UndefinedError

from src import utils


@pytest.mark.parametrize(
    "file_path,kwargs,error",
    [
        ("www/html/header.html", {}, UndefinedError),
        ("www/html/header.html", {"region": "foo"}, UndefinedError),
        ("www/html/header.html", {"region": "foo", "title": "bar"}, None),
        (
            "www/html/header.html",
            {"region": {"title": "foo", "href": "baz"}, "title": "bar"},
            None,
        ),
        ("www/html/footer.html", {}, None),
    ],
)
def test_include_html(file_path: str, kwargs: dict, error: Any):
    if error is not None:
        with pytest.raises(error):
            utils.include_html(file_path, **kwargs)
    else:
        assert utils.include_html(file_path, **kwargs)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("foo", "Foo"),
        ("foo_bar", "Foo Bar"),
        ("foo___bar", "Foo   Bar"),
        ("foo bar", "Foo Bar"),
        ("foo_bar BAZ", "Foo Bar Baz"),
    ],
)
def test_unsnake(text: str, expected: str):
    assert utils.unsnake(text) == expected
