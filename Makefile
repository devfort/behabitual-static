.PHONY: all clean server watch

all:
	python gamgee/generate.py

clean:
	find dest -name '*.html' -or -name '*.css' | xargs rm

server:
	python -m http.server --directory ./dest

watch:
	find src -not -path '*/\.' | entr make clean all
