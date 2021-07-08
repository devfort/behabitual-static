.PHONY: all clean server watch

all:
	python gamgee/generate.py

clean:
	find dest -type f -not -name '.gitignore' | xargs rm

server:
	python -m http.server --directory ./dest

watch:
	find src -not -path '*/\.' | entr make clean all
