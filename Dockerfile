FROM python:3-slim
# demisto/fastapi:0.120.1.5622230

WORKDIR /app
# installing requirements
# COPY ./requirements.txt ./requirements.txt

# RUN export PATH=$PATH:/usr/local/mysql/bin

# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# copying project to image
COPY ./config.py .
COPY ./main.py .
COPY ./venv ./venv

# venv
# RUN python3 -m venv ./venv
RUN ls
RUN . /app/venv/bin/activate




# forwarding ports
EXPOSE 8000

# ENTRYPOINT ["fastapi", "run", "main.py"]