book= input("What type of book is this?")
#print the user input
print(book)
#check the user input against our list of preferred genres
if book == "adventure" or book == "comedy":
    print(f"I like {book} books")
else:
    print(f"I do not like reading books.")