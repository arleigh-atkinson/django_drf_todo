# Start with python
FROM python:3.6

# Install dependencies
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose and run
EXPOSE 8000
CMD ["django-admin", "runserver"]
