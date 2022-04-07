FROM python:3.9

WORKDIR /app/back

COPY requirements.txt ./
COPY entrypoint.sh ./

RUN python -m pip install --upgrade pip
RUN pip install --upgrade virtualenv
RUN pip install -r requirements.txt
RUN chmod +x ./entrypoint.sh

COPY . ./

ENTRYPOINT ["sh", "/app/back/entrypoint.sh"]
