FROM python
WORKDIR /test
COPY ./requirements.txt /test/requirements.txt
RUN pip install -r /test/requirements.txt
COPY ./src /test/src
CMD [ "uvicorn","main:app","--port","8000"]