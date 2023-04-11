FROM node:19-alpine
USER root
WORKDIR /frontend
COPY --chown=node:node ./frontend/package*.json ./
RUN apk update \
    && apk add --no-cache --virtual .build-deps python3 make g++ git \
    && npm install \
    && apk del .build-deps
USER node
CMD ["npm", "run", "start"]