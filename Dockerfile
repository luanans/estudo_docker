FROM python

WORKDIR /app

COPY requirements.txt .
COPY modelo.py .

RUN pip install -r requirements.txt

CMD ["python", "./modelo.py"]