FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    --trusted-host pypi.python.org

COPY . . 

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

EXPOSE 8080