FROM python:3.10-slim
WORKDIR /API
COPY . /API
EXPOSE 5000
RUN pip install flask
CMD ["python3","app.py"]