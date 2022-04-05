FROM python:3.9

RUN mkdir /app
WORKDIR /app

RUN pip install --user Flask==2.0.3

RUN pip install redis

RUN wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

COPY app.py /app/app.py

RUN chmod +rx /app/app.py

ENTRYPOINT ["python"]
CMD ["app.py"]