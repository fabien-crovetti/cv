FROM nginx:1.26.0-alpine

COPY ./docker/nginx/default.conf /etc/nginx/conf.d/default.conf

COPY ./dist /srv/public

RUN chmod -R 755 /srv/public