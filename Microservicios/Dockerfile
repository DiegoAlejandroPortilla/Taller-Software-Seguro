# For more information, please refer to https://aka.ms/vscode-docker-python
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

EXPOSE 8001


# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN python

WORKDIR /app
COPY . /app
COPY main.py .
COPY methods ./methods
COPY routes ./routes
COPY schemas ./schemas 
COPY config ./config


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8001"]


