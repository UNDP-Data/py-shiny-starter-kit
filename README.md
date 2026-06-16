# py-shiny-starter-kit

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FUNDP-Data%2Fpy-shiny-starter-kit%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)
[![License](https://img.shields.io/github/license/undp-data/py-shiny-starter-kit)](https://github.com/undp-data/py-shiny-starter-kit/blob/main/LICENSE)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

Project template for creating [Shiny for Python](https://shiny.posit.co/py/) applications in line with the [UNDP Design System](https://design.undp.org). This project supercedes [st-undp](https://github.com/UNDP-Data/st-undp) and is strongly recommended for developing new data apps at UNDP.

> [!NOTE]  
> **Disclaimer:**
Posit, RStudio, and Shiny are trademarks of Posit Software, PBC, all rights reserved, and may be registered in the United States Patent and Trademark Office and in other countries. This project is not affiliated with, endorsed by, or directly supported by Posit Software, PBC.

## Table of Contents

- [Overview](#overview)
- [Getting started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

To use the template you need to follow a few simple steps:

1. Create a new repository from the template.
2. Define your dependencies.
3. Create a virtual environment.
4. Adapt the codebase to your needs.
5. Deploy the application.

See the sections below to understand each of these steps.

## Getting started

Use this repository to bootstrap your project
by [creating a new repository from the template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template). Once you have created the new repository, [clone it to your machine](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) and navigate to the project directory (or open the project in an IDE of your choice).

## Installation

Use a terminal (or your IDE) to set up a local Python environment. The template ships `pyproject.toml` with both core and optional dependencies. If you need additional packages for your project, you can add them to the dependencies section:

```diff
dependencies = [
    "shiny[theme] == 1.6.1",
    "shinywidgets == 0.8.1",
    "pandas ~= 3.0.2",
+    "scikit-learn == 1.8.0",
     ...
]
```

> [!TIP]
> For extra details on how to configure `pyproject.toml`, refer to [Python Packaging User Guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#dependencies-and-requirements).

Once the dependencies are defined, use `venv` to [create a virtual environment](https://docs.python.org/3.13/library/venv.html#creating-virtual-environments):

```sh
# Create and activate an environment (POSIX only)
python -m venv .venv
source .venv/bin/activate
```

> [!CAUTION]
> On some platforms, including Windows, the activation command is different. Refer to [How venvs work](https://docs.python.org/3.13/library/venv.html#how-venvs-work) section for details. If you use VS Code, you can also benefit from [Quick Create](https://code.visualstudio.com/docs/python/environments#_create-delete-and-manage-environments) command to create the environment.

In the activated environment, run the below command to install core and development dependencies:

```sh
pip install ".[dev]"
```

> [!TIP]
> In case you are an advanced user, you can use `poetry` to [manage your environment](https://python-poetry.org/docs/managing-environments/) or other tools if you prefer.

## Usage

**Running the app**

Once the dependencies are installed, you can run the application with:

```sh
shiny run -r app.py
```

which should launch the app at http://127.0.0.1:8000. With the `-r` flag, the application will track changes to the source code (inside `app.py` or `src` folder) and refresh the page whenever modifications are detected.

**Configuring metadata**

Using [`_brand.yml`](./_brand.yml), you can easily change basic app metadata, such as logo version, titles and links in the header:

```yaml
meta:
  header:
    region:
      text: LACRO
      href: "https://www.undp.org/latin-america"
    title:
      text: New App Name
      href: "#"
    logo: pnud
  footer:
    logo: pnud
```

**Managing the layout**

The template comes in a "multi-page" layout that uses hidden tabs. You can add new pages to the header and define their corresponding logic with [Shiny Modules](https://shiny.posit.co/py/docs/modules.html). Check out [`src/modules.example.py`](./src/modules/example.py) for an actual implementation.

> [!CAUTION]
> When using the tabs, you must ensure that the values passed to `navs` argument in `components.header` match those used for `ui.nav_panel`. Otherwise, the page switching logic won't work as expected.

If you are building a simple app that does not require multiple views, you can simplify the `app_ui` in [`app.py`](./app.py) as follows:

```python
app_ui = ui.page_fluid(
    ui.head_content(*link_undp_css(), *link_undp_js()),
    components.header(**theme.brand.meta.header),
    modules.example.get_ui("page1"),
    components.footer(**theme.brand.meta.footer),
    theme=theme,
)
```

and remove `switch_page` callback altogether.

## Features

This template aims to provide the starter codebase for building Shiny for Python applications compliant with the UNDP Design System. It relies on two core packages:

- [`undp-design-system`](https://github.com/UNDP-Data/py-shiny-components) that implements custom components for Shiny for Python.
- [`undp-brand-yml`](https://github.com/UNDP-Data/undp-brand-yml) that provides a custom theme and unified branding definitions. It also provides a UNDP theme for `plotly` based on the [UNDP Data Visualisation Library](https://data-viz.data.undp.org).

> [!TIP]  
> If you utilise a data visualisation package other than `plotly`, you can use the `undp-brand-yml` package to create a custom theme. Visit the package's repository for more details.

## Testing

The project includes examples of basic unit and end-to-end tests. You may need to [install browsers](https://playwright.dev/python/docs/browsers) with `playwright` before you can run those.

## Contributing

All contributions must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). The codebase is formatted with `black` and `isort`. Use the provided [Makefile](./Makefile) for these routine operations.

1. Clone or fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Ensure your code is properly formatted (`make format`).
5. Commit your changes (`git commit -m 'Add some feature'`).
6. Push to the branch (`git push origin feature-branch`).
7. Open a pull request.

## License

This project is licensed under the BSD 3-Clause License. However, entities or individuals not affiliated with UNDP are strictly prohibited from using this package or any of its components to create, share, publish, or distribute works that resemble, claim affiliation with, or imply endorsement by UNDP.

UNDP’s name, emblem and its abbreviation are the exclusive property of UNDP and are protected under international law. Their unauthorized use is prohibited, and they may not be reproduced or used in any manner without UNDP’s prior written permission.

## Contact

If you are facing any issues or would like to make some suggestions, feel free to [open an issue](https://github.com/undp-data/py-shiny-starter-kit/issues/new/choose).
