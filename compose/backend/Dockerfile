FROM python:3.6-alpine

RUN apk update \
  && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev \
  && apk add --no-cache postgresql-dev

COPY backend/requirements/base.txt /base.txt
COPY backend/requirements/docker.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY compose/backend/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY compose/backend/start /start
RUN chmod +x /start

COPY ./backend /apps/backend
COPY ./backend/settings/settings_docker.py /apps/backend/settings/settings.py

WORKDIR /apps

ENTRYPOINT ["/entrypoint"]
