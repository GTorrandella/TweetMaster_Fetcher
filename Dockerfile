FROM python:3.5

WORKDIR usr/src/app

COPY requirements.txt ./requirements.txt
COPY /Fetcher ./Fetcher
COPY /Tweet ./Tweet
COPY /Campaign ./Campaign

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "-m", "Fetcher.fetcher_flask"]

