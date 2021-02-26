dev:
	docker-compose up
	inotifywait -q -m -e close_write ./**/* | while read file; do \
		docker-compose up; \
	done
fix:
	docker-compose build --build-arg TOKEN=${TOKEN}
	docker build -t dragonmenorka/xstore-discord .
prod:
	docker run dragonmenorka/xstore-discord