FROM python:3.9

ADD Kv_store.py .

CMD ["python", "./Kv_store.py"]

EXPOSE 1024
