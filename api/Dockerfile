FROM python:3.7.6

RUN mkdir /api
WORKDIR /api

COPY requirements.txt /api/requirements.txt

RUN pip install --no-deps -r requirements.txt

EXPOSE 6543

CMD ["python", "boot.py"]

