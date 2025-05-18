FROM python:3.7 AS builder

WORKDIR /usr/src/app

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip

COPY . .
# Fix the code before installing to avoid issues with FastAPI parameter annotations
RUN python fix_fastapi_annotations.py

# Install a compatible version of FastAPI that works better with Python 3.7
RUN pip install fastapi==0.95.2 pydantic==1.10.8 typing-extensions==4.7.1
RUN pip install --no-cache-dir .


FROM python:3.7 AS test_runner
WORKDIR /tmp
COPY --from=builder /venv /venv
COPY --from=builder /usr/src/app/tests tests
ENV PATH=/venv/bin:$PATH

# install test dependencies
RUN pip install pytest

# We can now run tests with the fixed FastAPI version
RUN pytest tests


FROM python:3.7 AS service
WORKDIR /app
COPY --from=builder /venv /venv
COPY --from=builder /usr/src/app/src/openapi_server /app/openapi_server
ENV PATH=/venv/bin:$PATH

# Command to run when the container starts
CMD ["uvicorn", "openapi_server.main:app", "--host", "0.0.0.0", "--port", "8080"]
