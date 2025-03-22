class VoiceChannelCog:
    def __init__(self, bot):
        self.bot = bot

    async def on_voice_state_update(self, member, before, after):
        if after.channel is not None and after.channel.name == "Join to create":
            # Create a temporary voice channel
            guild = member.guild
            channel_name = f"{member.name}'s Channel"
            temp_channel = await guild.create_voice_channel(channel_name)

            # Move the member to the new channel
            await member.move_to(temp_channel)

            # Set up a listener to delete the channel when empty
            def check_channel_empty():
                return len(temp_channel.members) == 0

            await self.bot.wait_until(check_channel_empty())
            await temp_channel.delete()