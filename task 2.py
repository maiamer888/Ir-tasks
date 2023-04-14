import nltk

# get text input from user
text = input("Enter some text: ")

# tokenize the text into words and sentences
words = nltk.word_tokenize(text)
sentences = nltk.sent_tokenize(text)

# ask the user for their choice
choice = input("Enter your choice (1 for tokenized words, 2 for tokenized sentences, 3 for original text): ")

# print output based on user choice
if choice == '1':
    print(words)
elif choice == '2':
    print(sentences)
elif choice == '3':
    print(text)
else:
    print("Invalid choice.")