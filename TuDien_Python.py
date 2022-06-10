from fnmatch import translate


vocabulary = {
    "Happy":"Vui Ve"
}

def get_vocabulary_data(vocab_db, vocab):
    for item in vocab_db:
        if item == vocab:
            print(item, " : ", vocab_db[item])
        else:
            print(input_word, " doesn't exits ")

input_word = input("Enter the word you want: ")
translated_word = get_vocabulary_data(vocabulary, input_word)

if translated_word:
    print(translated_word)
    
