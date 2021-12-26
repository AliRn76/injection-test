FROM python:3.8
ENV PYTHONUNBUFFERED 1

COPY start /usr/local/bin/
RUN chmod +x /usr/local/bin/start
RUN ln -s /usr/local/bin/runner /bin/start

RUN mkdir /injection
WORKDIR /injection
COPY . /injection/

RUN pip install -U pip
RUN pip install -r requirements.txt
CMD ["start"]
