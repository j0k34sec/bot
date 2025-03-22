def set_limit(channel, limit):
    """
    Sets the user limit for the specified voice channel.

    Parameters:
    channel (discord.VoiceChannel): The voice channel to update.
    limit (int): The new user limit for the voice channel.
    """
    if limit < 0:
        raise ValueError("Limit must be a non-negative integer.")
    
    # Update the channel's user limit
    await channel.edit(user_limit=limit)