import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emoji(emoji_count):
    emojis = "😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗"
    emoji = ""
    for i in range(emoji_count):
        emoji += random.choice(emojis)
    return emoji