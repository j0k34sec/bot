def invite_member(bot, ctx, member_name):
    # Fetch the member from the guild
    member = ctx.guild.get_member_named(member_name)
    
    if member is None:
        return ctx.send(f"Member '{member_name}' not found.")
    
    # Check if the voice channel is private and if the user has permission
    voice_channel = ctx.author.voice.channel
    if voice_channel.permissions_for(ctx.author).connect:
        # Send a direct message to the invited member
        try:
            await member.send(f"You have been invited to join {voice_channel.name}.")
            await ctx.send(f"Invitation sent to {member_name}.")
        except Exception as e:
            await ctx.send(f"Failed to send invitation to {member_name}. Error: {str(e)}")
    else:
        await ctx.send(f"You do not have permission to invite members to {voice_channel.name}.")