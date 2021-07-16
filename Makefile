# i.e. make
.DEFAULT_GOAL := test

.PHONY: src test

sh:
	docker-compose run --rm app bash

test:
	docker-compose run --rm app pytest

lint:
	docker-compose run --rm app pylint src

build:
	@docker-compose build app
