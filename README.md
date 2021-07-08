# Gamgee

This is a static version of [Hobbit](https://github.com/devfort/behabitual)
which previously ran [BeHabitual](https://www.behabitual.com).

The dynamic version of BeHabitual has retired, and this mostly static site
has replaced it.

The small amount of Python code in this repo helps to ease the Hobbit into its
retirement, by allowing us to re-use some Django templates, tweaked to run in
Jinja2.


## Usage

You need a few things installed in order to work on this site:

- Python 3
- Jinja2, e.g. via `pip install jinja2`
- libsass, e.g. via `pip install libsass`
- entr(1), if you want to quickly see your changes

To make changes to the static site:

1. Change the files in the `src` directory.
2. Run `make clean all`
3. Deploy the generated files from the `dest` directory to your host of choice.

Any file in `src/pages` will produce a corresponding file in `dest`, e.g.
`src/pages/index.html` will produce `dest/index.html`.

Other files in `src` provide layouts, reusable partial templates, etc.

If you're making lots of changes, there are some additional Makefile targets to
make your life easier:

- `make watch` will run `make clean all` whenever a file in `src` changes.
- `make server` will run an HTTP server on port 8000 where you can browse the
  site.
