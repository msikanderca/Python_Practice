# emoji conversion
message = input ( "Enter data : ")
words = message. split (' ')
emojis = {
    ":)" : "smile",
    ":(" : "sad"
}
output = ""
for data  in words:
    output =output + emojis.get (data,data) + " "
print(output)

