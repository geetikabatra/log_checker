.PHONY: all generate clean docker

all: clean generate docker

generate:
	@echo "Creating empty access log to mount"
	mkdir tmp
	touch tmp/access.log

docker:
	@echo "Building docker images"
	docker-compose build
	docker-compose up

clean:
	@echo "Cleaning up..."
	rm -rf tmp/
