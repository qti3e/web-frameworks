FROM python

WORKDIR /usr/src/app

COPY requirements.txt settings.py ./
COPY app app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD gunicorn --bind 0.0.0.0:3000 --worker-class gunicorn.workers.ggevent.GeventWorker --reuse-port --workers $(nproc) app.wsgi
