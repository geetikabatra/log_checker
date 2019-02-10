.PHONY: all generate clean

all: generate clean

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
