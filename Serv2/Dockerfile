FROM python:3.8-slim

EXPOSE 8000

ARG URL
ENV URL=${URL}

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . ./app

CMD [ "python", "main.py" ]