message = input('>')
messsage1 = message.split(' ') 

emojis = {
    ":)":"🙂",
    ":(":"🙁"
}
output = ""
for word in messsage1:
    output += emojis.get(word, word) + " "
print(output)