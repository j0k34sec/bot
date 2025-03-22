# Discord Temporary Voice Channel Bot

This Discord bot automatically creates temporary voice channels when members join a specific voice channel. It is designed to enhance the user experience in Discord servers by providing dynamic voice channel management.

## Features

- Automatically creates a temporary voice channel when a member joins a designated voice channel.
- Deletes the temporary voice channel when it becomes empty.
- Customizable settings for voice channel creation.

## Requirements

- Python 3.8 or higher
- Discord.py library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/discord-bot.git
   cd discord-bot
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Discord bot:
   - Create a new bot on the Discord Developer Portal.
   - Copy the bot token and add it to your environment variables or directly in the code (not recommended for production).

4. Run the bot:
   ```
   python src/bot.py
   ```

## Usage

- Invite the bot to your server using the OAuth2 URL generated in the Discord Developer Portal.
- Configure the bot's settings in the code to specify which voice channel should trigger the creation of temporary channels.

## Contributing

Feel free to submit issues or pull requests to improve the bot's functionality. 

## License

This project is licensed under the MIT License.