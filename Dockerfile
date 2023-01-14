FROM python:3.8-alpine

# Install git
RUN apk update && apk add git

# Create app directory
WORKDIR /usr/src/app

# Clone the repository
RUN git clone https://github.com/crisco00xd/chatgpt-discord-bot.git .

# Copy requirements.txt and install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the bot
CMD ["python", "smart_bot.py"]
