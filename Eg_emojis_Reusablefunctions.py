# emoji conversion with resuable functions
def emoji_converter (message):
    words = message.split(' ')
    emojis = {
        ":)": "smile",
        ":(": "sad"
    }
    output = ""
    for data in words:
        output = output + emojis.get(data, data) + " "
    return output


message = input ( "Enter data : ")
print(emoji_converter(message))

