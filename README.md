# Gamgee

This is a static version of [Hobbit](https://github.com/devfort/behabitual)
which previously ran [Be Habitual](https://www.behabitual.com).

The dynamic version of Be Habitual has retired, and this static site
has replaced it.

The small amount of Python code in this repo helps to ease the Hobbit into its
retirement, by allowing us to re-use some Django templates, tweaked to run in
Jinja2.


## Structure

In general: files from `src` and compiled to a static site in `dest`, which can
then be deployed.

Any file in `src/html/pages` will produce a corresponding file in `dest`, e.g.
`src/html/pages/index.html` will produce `dest/index.html`.
Other files in `src/html` provide layouts, reusable partial templates, etc.

CSS is generated from `src/scss`, with `src/scss/_manifest.scss` used as the
entry-point, producing `dest/hobbit.css`.

Any files in `src/static` are recursively copied into the compiled site, e.g.
`src/static/images/edit.png` is copied to `dest/images/edit.png`.


## Usage

You need a few things installed in order to work on this site:

1. Python 3
2. Jinja2 & libsass: `pip install -r requirements.txt`
3. [entr(1)][1], if you want to use `make watch` quickly see your changes

[1]: http://eradman.com/entrproject/

To make changes to the static site:

1. Change the files in the `src` directory.
2. Run `make clean all`
3. Deploy the generated files from the `dest` directory to your host of choice.

If you're making lots of changes, there are some additional Makefile targets to
make your life easier:

- `make watch` will run `make clean all` whenever a file in `src` changes.
- `make server` will run an HTTP server on port 8000 where you can browse the
  site.


## Hosting

The static site is currently hosted by @georgebrock, with `make deploy`
configured to deploy to one of his servers.
