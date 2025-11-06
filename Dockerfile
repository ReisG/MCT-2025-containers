FROM python:3-slim

CMD ["pip", "install", "-r", "requiremets.txt"]
EXPOSE 8000

WORKDIR /app
COPY . .

ENTRYPOINT ["fastapi", "run", "main.py"]