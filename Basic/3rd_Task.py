def word_counter(filename):
    try:
        with open(filename,'r') as OpenedFile:
            WordCount=0
            for items in OpenedFile:
                words=items.split()
                WordCount+=len(words)
            else:
                return WordCount
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return 0
file=(input("Enter name of the file (with extension): "))
total_words=word_counter(file)
if total_words > 0:
    print(f"The total number of words in {file} is: {total_words}")