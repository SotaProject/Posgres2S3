FROM python:3.12-alpine

RUN apk add postgresql16-client

COPY . .

RUN pip install -r requirements.txt

RUN crontab crontab

CMD ["crond", "-f"]