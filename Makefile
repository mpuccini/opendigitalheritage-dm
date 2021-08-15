app_name = poc-eneahs
env_file = app/.env

build: 
	@echo 'Buinding container...'
	@docker build -t $(app_name) .

run-fs: 
	@echo 'Run container with fs support...'
	@docker run --detach -p 5000:5000 -v $(FS_PATH):/$(FS_PATH):Z --env-file=$(env_file) $(app_name)

run-s3: 
	@echo 'Run container with S3 support...'
	@docker run --detach -p 5000:5000 -v $(HOME)/.aws/credentials:/root/.aws/credentials --env-file=$(env_file) $(app_name)

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
