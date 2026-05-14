"""
Basic end-to-end test for the app.
"""

from playwright.sync_api import Page, expect
from shiny.playwright import controller
from shiny.pytest import create_app_fixture
from shiny.run import ShinyAppProc

# Overwrite the expected location of the enrty point
app = create_app_fixture("../app.py")


def test_basic_app(page: Page, app: ShinyAppProc) -> None:
    """
    E2e test for the module page.
    """
    # Navigate to the app URL when it's ready
    page.goto(app.url)

    # Get the hold of the controlers
    selectesize = controller.InputSelectize(page, "page1-species")
    slider = controller.InputSliderRange(page, "page1-sepal_lengths")

    # Get the hold of the outputs
    plot = page.locator("#page1-plot .main-svg").last
    table = controller.OutputDataFrame(page, "page1-table")

    # Ensure the outputs are rendered
    expect(plot).to_be_visible(timeout=3000)  # Wait for 3 seconds
    table.expect_nrow(150)

    # Test if the filters are working
    selectesize.set(["setosa"])
    table.expect_nrow(50)

    selectesize.set(["setosa", "versicolor"])
    table.expect_nrow(100)

    selectesize.set(["virginica"])
    slider.set(("5", "6"))
    table.expect_nrow(8)
