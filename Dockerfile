FROM python:3.9.6-slim-buster

EXPOSE 80

RUN mkdir /code
WORKDIR /code
ADD . /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python","./main.py"]