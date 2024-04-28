FrOM python:3.10.11

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
