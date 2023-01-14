#🤖 Discord Smart Bot
##A Discord bot that uses the OpenAI API to generate human-like responses to prompts.

#Features
- Generate responses to prompts using the OpenAI API
- Change the temperature of the responses (affects the creativity of the responses)
- Split long responses into chunks to avoid message length limits

###How it works
The bot listens for commands starting with the ! prefix and responds accordingly.

Currently, there are two commands:

- `!smart <prompt>` - generates a response to the given prompt
- `!temp <value>` - changes the temperature of the responses (affects the creativity of the responses)

How to run using python

Clone the repository
```git clone https://github.com/crisco00xd/chatgpt-discord-bot.git```

Install the dependencies
```pip install -r requirements.txt```

Set your OpenAI API key and Discord API key in the smart_bot.py file

Run the bot
```python smart_bot.py```

How to host on a docker container

Build the image
```docker build -t <image-name> . ```

Run the container
```docker run -d --env OPENAI_API_KEY=<your_api_key> --env DISCORD_API_KEY=<your_discord_api_key> <image-name>```

Make sure to replace <your_api_key> and <your_discord_api_key> with your actual OpenAI and Discord API keys.

Note
This bot requires OpenAI API Key and Discord API key, please make sure to have both keys before running the bot.
