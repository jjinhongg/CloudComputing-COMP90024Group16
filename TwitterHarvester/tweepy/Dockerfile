# Group 16

# Team members:

# Zenan Ji (Student ID: 1122396) - city: Nanjing

# Weijie Ye (Student ID: 1160818) - city: Fuzhou

# Wenqin Liu (Student ID: 807291) - city: Guangdong

# Jinhong Yong (Student ID: 1198833) - city: Kuala Lumpur

# Zixuan Zeng (Student ID: 1088297) - city: Melbourne

FROM python:3.8.2

# there lines are dedicate for nectar server
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
