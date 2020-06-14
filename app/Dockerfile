# Builder

FROM python:3 as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

# install deps
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# Final

FROM python:3

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system app && usermod -G app app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# install dependencies
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

RUN chown -R app:app $APP_HOME
USER app

RUN chmod +x start_scrapping.sh

ENTRYPOINT [ "/home/app/web/entrypoint.sh" ]
