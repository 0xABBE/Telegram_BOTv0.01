FROM python:3.9-slim 

RUN mkdir /workspace/ && cd /workspace/ 
RUN python install -r requirements.txt

WORKDIR /workspace

CMD ["python3","bot.py"]
