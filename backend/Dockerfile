FROM python:3

WORKDIR /src

EXPOSE 8080

COPY requirements.txt ./
RUN curl https://bootstrap.pypa.io/get-pip.py | python3
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python3 src/app.py