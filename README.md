# Gamgee

This is a static version of [Hobbit](https://github.com/devfort/behabitual)
which previously ran [BeHabitual](https://www.behabitual.com).

The dynamic version of BeHabitual has retired, and this mostly static site
has replaced it.

The small amount of Python code in this repo helps to ease the Hobbit into its
retirement, by allowing us to re-use some Django templates, tweaked to run in
Jinja2.


## Usage

To make changes to the static site:

0. Install Jinja2: `pip install jinja2`.
1. Change the files in the `src` directory.
2. Run `python gamgee/generate.py`
3. Deploy the generated files from the `dest` directory to your host of choice.

Any file in `src/pages` will produce a corresponding file in `dest`, e.g.
`src/pages/index.html` will produce `dest/index.html`.

Other files in `src` provide layouts, reusable partial templates, etc.
