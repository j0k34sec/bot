def reject_member(vc_creator, member):
    """
    Rejects a member from the voice channel.
    
    Parameters:
    vc_creator (Member): The creator of the voice channel.
    member (Member): The member to be rejected.
    
    Returns:
    str: A message indicating the result of the rejection.
    """
    if vc_creator.has_permission("manage_channel"):
        # Logic to remove the member's access to the voice channel
        # This would typically involve updating the channel's permissions
        # and notifying the member that they have been rejected.
        return f"{member.name} has been rejected from the voice channel."
    else:
        return "You do not have permission to reject members."