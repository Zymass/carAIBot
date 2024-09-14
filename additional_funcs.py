import re


def check_sub_channel(chat_member) -> bool:
    if chat_member.status != 'left':
        return True
    else:
        return False