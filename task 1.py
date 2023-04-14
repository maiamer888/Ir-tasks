import nltk

text = input("Enter some text: ")

print("Choose an option:")
print("1. Print tokenized words.")
print("2. Print tokenized sentences.")
print("3. Print original text.")

choice = int(input())

if choice == 1:
    words = nltk.word_tokenize(text)
    print(words)
elif choice == 2:
    sentences = nltk.sent_tokenize(text)
    print(sentences)
elif choice == 3:
    print(text)
else:
    print("Invalid choice.")