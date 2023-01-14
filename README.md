# 🤖 Discord Smart Bot
## A Discord bot that uses the OpenAI API to generate human-like responses to prompts.

# Features
- Generate responses to prompts using the OpenAI API
- Change the temperature of the responses (affects the creativity of the responses)
- Split long responses into chunks to avoid discord's message length limits

# How it works
The bot listens for commands starting with the ! prefix and responds accordingly.

Currently, there are two commands:

- `!smart <prompt>` - generates a response to the given prompt
- `!temp <value>` - changes the temperature of the responses (affects the creativity of the responses)

> Max and Min temperature values are 0.1 and 2.0.

## How To Run Using Python

1. Clone the repository
```git clone https://github.com/crisco00xd/chatgpt-discord-bot.git```

2. Install the dependencies
```pip install -r requirements.txt```

3. Set your OpenAI API key and Discord API key in the smart_bot.py file

4. Run the bot
```python smart_bot.py```

## How To Host On a Docker Container

1. Build the image
```docker build -t <image-name> . ```

2. Run the container
```docker run -d --env OPENAI_API_KEY=<your_api_key> --env DISCORD_API_KEY=<your_discord_api_key> <image-name>```

> Make sure to replace <your_api_key> and <your_discord_api_key> with your actual OpenAI and Discord API keys.

## Running the Bot with Docker Compose

1. Make sure you have Docker Compose installed on your system.

2. Replace YOUR_API_KEY with your actual OpenAI and Discord API keys in the docker-compose.yml file.

3. Start the bot by running the following command in the same directory as the docker-compose.yml file:
```docker-compose up -d```

This command will start the bot in detached mode, you can check the logs by running `docker-compose logs -f`

4. To stop the bot, run the following command:
```docker-compose down```

You should now have the bot running in a Docker container, ready to respond to commands on your Discord server.




# Note
## This bot requires OpenAI API Key and Discord API key, please make sure to have both keys before running the bot.
