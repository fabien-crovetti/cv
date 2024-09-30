FROM node:20.17.0-bullseye

WORKDIR /srv

RUN corepack enable

COPY docker-entrypoint.sh /docker-entrypoint

RUN chmod 755 /docker-entrypoint


ENTRYPOINT ["/docker-entrypoint"]

CMD ["yarn", "run", "dev", "--host"]

