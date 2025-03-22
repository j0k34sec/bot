def forcemute(channel, mute: bool):
    """
    Force mutes or unmutes all members in the specified voice channel.
    
    Parameters:
    - channel: The voice channel to mute or unmute.
    - mute: A boolean indicating whether to mute (True) or unmute (False) the members.
    """
    for member in channel.members:
        if mute:
            # Mute the member
            member.edit(mute=True)
        else:
            # Unmute the member
            member.edit(mute=False)