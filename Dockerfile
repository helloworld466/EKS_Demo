FROM python:rc-slim-buster
WORKDIR app
COPY ./sample.py /app/sample.py
COPY ./start.sh /app/start.sh
RUN chmod +x start.sh && pip install flask
EXPOSE 5000
CMD ["/app/start.sh"]