FROM python:3.7-alpine

EXPOSE 4000

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY src/ /src
WORKDIR /app

ENTRYPOINT ["python", "src/index.py"]
