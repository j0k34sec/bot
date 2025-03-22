def permit_member(bot, ctx, member: str):
    """Permit a member to join the private voice channel."""
    # Get the voice channel of the command context
    voice_channel = ctx.author.voice.channel

    # Check if the voice channel exists and the command issuer is the creator
    if voice_channel and ctx.author == voice_channel.creator:
        # Get the member to permit
        member_to_permit = ctx.guild.get_member_named(member)

        if member_to_permit:
            # Update the channel permissions to allow the member
            await voice_channel.set_permissions(member_to_permit, connect=True)
            await ctx.send(f"{member} has been permitted to join the voice channel.")
        else:
            await ctx.send(f"Member {member} not found.")
    else:
        await ctx.send("You do not have permission to permit members in this channel.")