FROM python:3.8-slim

# Create app directory
WORKDIR /config

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Start the bot
CMD ["python", "smart_bot.py"]