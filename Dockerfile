FROM python:3.11

RUN pip install playwright
RUN playwright install
