include .env
.DEFAULT_GOAL:=help

# Credits: https://github.com/sherifabdlnaby/elastdocker/

# This for future release of Compose that will use Docker Buildkit, which is much efficient.
COMPOSE_PREFIX_CMD	:= COMPOSE_DOCKER_CLI_BUILD=1
COMPOSE_CMD 		:= docker compose
COMPOSE_ALL_FILES	:= -f docker-compose.yml
COMPOSE_DEV_ALL_FILES := -f docker-compose.dev.yml
SERVICES         	:= db web proxy redis celery celery-beat ollama

# --------------------------

.PHONY: setup certs up build username pull down stop restart rm logs

certs:		    ## Generate certificates.
	@${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} -f docker-compose.setup.yml run --rm certs

setup:			## Generate certificates.
	@make certs

up:				## Build and start all services.
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} ${COMPOSE_ALL_FILES} up -d --build ${SERVICES}

build:			## Build all services.
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} ${COMPOSE_ALL_FILES} build ${SERVICES}

username:		## Generate Username (Use only after make up).
ifeq ($(isNonInteractive), true)
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} ${COMPOSE_ALL_FILES} exec web poetry -C /home/rengine run python3 manage.py createsuperuser --username ${DJANGO_SUPERUSER_USERNAME} --email ${DJANGO_SUPERUSER_EMAIL} --noinput
else
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} ${COMPOSE_ALL_FILES} exec web poetry -C /home/rengine run python3 manage.py createsuperuser
endif

changepassword:	## Change password for user
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} ${COMPOSE_ALL_FILES} exec web poetry -C /home/rengine run python3 manage.py changepassword

migrate:		## Apply migrations
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} ${COMPOSE_ALL_FILES} exec web poetry -C /home/rengine run python3 manage.py migrate

pull:			## Pull Docker images.
	# docker login docker.pkg.github.com
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} ${COMPOSE_ALL_FILES} pull

down:			## Down all services.
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} ${COMPOSE_ALL_FILES} down

stop:			## Stop all services.
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} ${COMPOSE_ALL_FILES} stop ${SERVICES}

restart:		## Restart all services.
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} ${COMPOSE_ALL_FILES} restart ${SERVICES}

rm:				## Remove all services containers.
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} $(COMPOSE_ALL_FILES) rm -f ${SERVICES}

test:
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} $(COMPOSE_ALL_FILES) exec celery poetry -C /home/rengine run python3 -m unittest tests/test_scan.py

logs:			## Tail all logs with -n 1000.
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} $(COMPOSE_ALL_FILES) logs --follow --tail=1000 ${SERVICES}

images:			## Show all Docker images.
	${COMPOSE_PREFIX_CMD} ${COMPOSE_CMD} $(COMPOSE_ALL_FILES) images ${SERVICES}

prune:			## Remove containers and delete volume data.
	@make stop && make rm && docker volume prune -f

help:			## Show this help.
	@echo "Make application Docker images and manage containers using Docker Compose files."
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m (default: help)\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

dev_build:			## Build all services.
	${COMPOSE_PREFIX_CMD} docker compose ${COMPOSE_DEV_ALL_FILES} build ${SERVICES_DEV}

dev_up:				## Build and start all services.
	${COMPOSE_PREFIX_CMD} docker compose ${COMPOSE_DEV_ALL_FILES} up -d --build ${SERVICES_DEV}

dev_down:			## Down all services.
	${COMPOSE_PREFIX_CMD} docker compose ${COMPOSE_DEV_ALL_FILES} down

dev_logs:			## Tail all logs with -n 1000.
	${COMPOSE_PREFIX_CMD} docker compose $(COMPOSE_DEV_ALL_FILES) logs --follow --tail=1000 ${SERVICES_DEV}
