def make_private(channel, creator):
    """
    Makes the specified voice channel private by updating its permissions.
    
    Args:
        channel: The voice channel to be made private.
        creator: The user who created the voice channel.
    """
    # Get the current permissions for the channel
    overwrites = channel.overwrites

    # Update permissions to make the channel private
    for overwrite in overwrites:
        if overwrite.id == channel.guild.id:  # Guild ID
            overwrite.deny.add(PermissionOverwrite(read_messages=False))
        elif overwrite.id == creator.id:  # Creator ID
            overwrite.allow.add(PermissionOverwrite(read_messages=True))

    # Apply the updated permissions to the channel
    await channel.edit(overwrites=overwrites)