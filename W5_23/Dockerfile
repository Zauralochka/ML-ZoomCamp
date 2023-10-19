FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["flask_serving.py", "test.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--listen=0.0.0.0:9696", "flask_serving:app"]