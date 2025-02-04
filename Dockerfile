# Use the official Airflow image with Python 3.12
FROM apache/airflow:2.9.1-python3.12

# Install Poetry (if not already available)
RUN pip install --upgrade pip && pip install poetry

# Set working directory and copy the Poetry files
WORKDIR /opt/airflow
COPY pyproject.toml poetry.lock* /opt/airflow/

# Configure Poetry to install packages into the system interpreter
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# Copy your DAGs and plugins into the image
COPY dags/ /opt/airflow/dags/
COPY plugins/ /opt/airflow/plugins/
