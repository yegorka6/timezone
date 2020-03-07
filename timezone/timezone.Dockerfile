FROM python:3.6

RUN pip install --upgrade pip

# Add a new non-root "app_user" with user id 3000
RUN useradd -u 3000 -m app_user

# Change to non-root privilege
USER app_user
WORKDIR /home/app_user

# Install dependencies
COPY --chown=app_user:app_user requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/app_user/.local/bin:/home/app_user/projects/api:/usr/bin/python:/usr/bin/python3:${PATH}"

COPY --chown=app_user:app_user ./projects/api /home/app_user

CMD ["python3", "api.py"]

