FROM node:20.19.0-bookworm

WORKDIR /srv

RUN corepack enable

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3-venv \
    && rm -rf /var/lib/apt/lists/*

COPY ./docker/node/docker-entrypoint.sh /docker-entrypoint

RUN chmod 755 /docker-entrypoint

ENTRYPOINT ["/docker-entrypoint"]

CMD ["yarn", "run", "dev", "--host"]
