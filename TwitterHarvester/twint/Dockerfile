FROM python:3

ENV http_proxy http://wwwproxy.unimelb.edu.au:8000
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000

RUN pip install -r stream_requirements.txt

CMD [ "python", "main.py"]