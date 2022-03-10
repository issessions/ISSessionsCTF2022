# Without quotes
cField = 3

with open("log.txt") as file:
    for l in file:
        fields = l.split(" ")
        word = fields[cField]
        if word[0] == "'":
            fields[cField] = str(ord(word[1]))
        
        print(" ".join(fields).strip())