dev:
	python3 main.py
	inotifywait -q -m -e close_write ./**/* | while read file; do \
		python3 main.py; \
	done
prod:
	python3 main.py