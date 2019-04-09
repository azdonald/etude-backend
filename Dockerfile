FROM python:3.6
RUN pip install -U pip
RUN pip install pipenv

COPY . /app
WORKDIR /app
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000



CMD [ "python", "manage.py", "run" ]

