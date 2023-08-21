FROM python:3

WORKDIR /condition_score_tracker

COPY ./requirements.txt /condition_score_tracker

RUN pip install -r /condition_score_tracker/requirements.txt

COPY . .