FROM python:3.10-alpine

COPY . .

EXPOSE 80

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
