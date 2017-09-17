FROM python:3.6

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		sqlite3 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV DJANGO_VERSION 1.11.5

RUN pip install django=="$DJANGO_VERSION"

WORKDIR /usr/src/app
