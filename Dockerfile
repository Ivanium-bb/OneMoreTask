FROM python:3.11.0rc2
WORKDIR /
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .