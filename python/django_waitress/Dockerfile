FROM python

WORKDIR /usr/src/app

COPY requirements.txt settings.py ./
COPY app app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD waitress-serve --host=0.0.0.0 --port=3000 --threads $(nproc) app.wsgi:application
