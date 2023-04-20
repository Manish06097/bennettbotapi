FROM python:3.8.5

# set work directory
WORKDIR /

# set env variables
RUN pip install --upgrade pip

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
