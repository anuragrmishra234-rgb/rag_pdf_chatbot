text = """
Python



is

awesome.


Page 5


"""

text = text.strip() #removes the unnecessay sapces

while "\n\n" in text:
    text = text.replace("\n\n","\n")    # removs the multiple lines

text = text.replace("\t"," ") #unnecessary tabs

while "  " in text:
    text = text.replace("  "," ")  #removes the spaces betwenn the words

print(text)