FROM python:rc-slim-buster
WORKDIR app
COPY ./flask.py /app/flask.py
COPY ./start.sh /app/start.sh
RUN chmod +x start.sh
EXPOSE 5000
CMD ["/app/start.sh"]

