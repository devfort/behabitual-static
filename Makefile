.PHONY: all clean server watch deploy

HOST=gamgee.georgebrock.com

all:
	python gamgee/generate.py

clean:
	find dest -type f -not -name '.gitignore' | xargs rm

server:
	python -m http.server --directory ./dest

watch:
	find src -not -path '*/\.' | entr make clean all

deploy: all
	scp nginx.conf $(HOST):/usr/local/www/behabitual.com/nginx.conf
	rsync -rv --delete dest/ $(HOST):/usr/local/www/behabitual.com/public_html/
	ssh $(HOST) "sudo /usr/local/etc/rc.d/nginx reload"
