#file = "python_text.txt"

f = open("text.txt", "w")
for i in range(1, 10):
    text = "Suck it up! I came " + str(i) + " times bitch \n"
    f.write(text)
f.close()