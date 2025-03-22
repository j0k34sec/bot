# Temporary Voice Channel Bot

This project is a Discord bot that allows users to create and manage temporary voice channels with various features. The bot provides commands for making voice channels private or public, setting member limits, permitting or rejecting members, forcing mute, and inviting users.

## Features

- **Temporary Voice Channels**: Create voice channels that disappear when the creator leaves.
- **Privacy Control**: Use `/private` to make a channel private and `/public` to make it public.
- **Member Limit**: Set a limit on the number of members in a voice channel using `/limit [limit number]`.
- **Member Management**: Permit or reject members from joining the voice channel with `/permit [member]` and `/reject [member name]`.
- **Force Mute**: Mute all members in the voice channel with `/forcemute [true or false]`.
- **Invitations**: Invite members to the voice channel using `/invite [username]`, with automatic permission handling for private channels.
- **Claiming Channels**: If the creator leaves, another member can claim the channel using `/claim`.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/temp-vc-bot.git
   ```

2. Navigate to the project directory:
   ```
   cd temp-vc-bot
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Discord bot and obtain the bot token.

5. Update the bot token in the `bot.py` file.

6. Run the bot:
   ```
   python src/bot.py
   ```

## Usage

Once the bot is running, you can use the following commands in a Discord server where the bot is present:

- `/private`: Make the current voice channel private.
- `/public`: Make the current voice channel public.
- `/limit [number]`: Set the maximum number of members allowed in the voice channel.
- `/permit [member]`: Allow a specific member to join the private voice channel.
- `/reject [member]`: Remove access for a specific member from the voice channel.
- `/forcemute [true/false]`: Mute or unmute all members in the voice channel.
- `/invite [username]`: Invite a user to the voice channel.
- `/claim`: Claim the voice channel if the creator has left.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.