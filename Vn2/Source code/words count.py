def word_count():
    text = input("Enter a string: ")
    words = text.split()
    count = len(words)
    print("The number of words in the string is:", count)

word_count()