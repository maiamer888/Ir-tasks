import nltk

text = input("Enter some text: ")

print("Choose an option:")
print("1. Print tokenized words.")
print("2. Print tokenized sentences.")
print("3. Print original text.")
print("4. Stemming")
print(" 4.1. Porter Stemmer")
print(" 4.2. Snowball Stemmer")

choice = int(input())

if choice == 1:
    words = nltk.word_tokenize(text)
    print(words)
    
elif choice == 2:
    sentences = nltk.sent_tokenize(text)
    print(sentences)
    
elif choice == 3:
    print(text)
    
elif choice == 4:
    word = input("Enter a word to stem: ")
    stemmer_choice = int(input("Choose a stemmer: \n1. Porter Stemmer\n2. Snowball Stemmer\n"))

    if stemmer_choice == 1:
        porter = nltk.PorterStemmer()
        stemmed_word = porter.stem(word)
        print(stemmed_word)
        
    elif stemmer_choice == 2:
        snowball = nltk.SnowballStemmer('english')
        stemmed_word = snowball.stem(word)
        print(stemmed_word)
        
    else:
        print("Invalid choice.")
        
else:
    print("Invalid choice.")

# Bonus task
import pandas as pd

data = pd.read_csv("data.csv")
null_rows = data.isnull().sum()
data = data.dropna()
print(f"Number of null rows removed: {null_rows.sum()}")