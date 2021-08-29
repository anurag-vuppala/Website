FROM python:3.7-slim as production

ENV PYTHONUNBUFFER=1
WORKDIR /app/

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY setup.cfg /setup.cfg
COPY mywebsite ./mywebsite
  
EXPOSE 8000

FROM production as devlopment

COPY requirements/dev.txt ./requirements/dev.txt
RUN pip install -r ./requirements/dev.txt