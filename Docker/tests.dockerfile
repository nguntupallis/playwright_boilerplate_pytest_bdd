FROM python:3.11

RUN apt-get update && apt-get install -y allure

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install tox

COPY . .

CMD ["tox"]
