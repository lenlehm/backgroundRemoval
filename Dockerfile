FROM python:3.6-slim
COPY ./requirements.txt /deploy/

COPY ./flask_service.py /deploy/
COPY ./preprocessing.py /deploy/
COPY ./u2_net_API.py /deploy/

COPY ./model /deploy/model
COPY ./saved_models /deploy/saved_models

WORKDIR /deploy/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
ENTRYPOINT ["python", "flask_service.py"]

