# latest python image
FROM python:latest

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
ENV DISPLAY=:99

# update pip and install dependencies
RUN pip install --upgrade pip
RUN pip install selenium
RUN pip install beautifulsoup4

# COPY the remote file at working directory in container
WORKDIR /app
COPY finn_problem_bingzhen.py ./

# enable run-time arguments
ENTRYPOINT ["python", "./finn_problem_bingzhen.py"]

# Then you can build an image from the Dockerfile and run a container from the image with run-time arguments. Like the following:
# docker build -t autoGoogleSearch
# docker run --rm autoGoogleSearch "Finn AI | The Leading" "AI chatbot" "bank chatbot"