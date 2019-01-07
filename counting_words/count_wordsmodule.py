def count_words(text: str, words: set):
    word_list = list(words)
    count = 0
    for i in range(len(word_list)):
         
        if(word_list[i] in text.lower()):
            print(word_list[i])
            count+=1
    return count
 
if __name__ == '__main__':
    print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit anything.",
                       {"sum", "hamlet", "infinity", "anything"}))