def check_permissions(member, permission):
    """Check if a member has a specific permission."""
    return getattr(member.guild.permissions, permission, False)

def format_channel_name(base_name, member_count):
    """Format the voice channel name based on the number of members."""
    return f"{base_name} ({member_count})"