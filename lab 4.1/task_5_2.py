def most_frequent_word():
    import string
    paragraph = input("Enter a paragraph: ").strip()
    # Convert to lowercase
    paragraph = paragraph.lower()
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    paragraph = paragraph.translate(translator)
    # Split into words
    words = paragraph.split()
    if not words:
        print("No words found.")
        return
    # Count frequency
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    # Find the most frequent word
    most_freq = max(freq, key=freq.get)
    print(most_freq)

most_frequent_word()

