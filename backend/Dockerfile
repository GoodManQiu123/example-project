FROM python:3.10

WORKDIR /backend

ENV TEST_MODE=False

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y ruby-full && gem install anystyle-cli

COPY ./app /backend/app

EXPOSE 8000

CMD ["python", "-m", "app.main"]
