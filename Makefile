app_name = poc-eneahs

build:
	@docker build -t $(app_name) .

run:
	@docker run --detach -p 5000:5000 $(app_name)

start:
	@echo 'Starting container...'
	@docker ps -a | grep $(app_name) | awk '{print $$1}' | xargs docker start

stop:
	@echo 'Stopping container...'
	@docker ps | grep $(app_name) | awk '{print $$1}' | xargs docker stop

kill:
	@echo 'Killing container...'
	@docker ps | grep $(app_name) | awk '{print $$1}' | xargs docker rm -f

clean:
	@echo 'Killing (eventually) dead container(s)...'
	@docker ps -a | grep $(app_name) | awk '{print $$1}' | xargs -r docker rm -f
	@echo 'Removing container image...'
	@docker images | grep $(app_name) | awk '{print $$3}' | xargs docker rmi