VOWELS = ('a', 'e', 'i', 'o', 'u')

def convert_word(word):
    first_letter = word[0]
    if first_letter in VOWELS:  # if word starts with a vowel...
        return word + "hay"     # then keep it as it is and add hay to the end
    else:
        return word[1:] + word[0] + "ay"    # like the lab mentions, word[1:]
                                            # returns the word except word[0]


# From this function, it's easy to take a sentence and convert it to Pig-Latin.

def convert_sentence(sentence):
    if sentence=="":
        return ""

    list_of_words = sentence.split(' ')
    new_sentence = ""   # we'll keep concatenating words to this...
    for word in list_of_words:
        new_sentence = new_sentence + convert_word(word)    # ...like this
        new_sentence = new_sentence + " "   # but don't forget the space!
    return new_sentence