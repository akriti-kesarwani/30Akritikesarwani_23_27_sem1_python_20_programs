def word_frequency(input_text):
    # Split the input text into words
    words = input_text.split()

    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    # Count the frequency of each word
    for word in words:
        # Remove punctuation and convert to lowercase for simplicity
        word = word.strip('.,!?()[]{}":;')
        word = word.lower()

        # Update the word frequency in the dictionary
        word_freq[word] = word_freq.get(word, 0) + 1

    # Sort the dictionary keys alphanumerically
    sorted_word_freq = dict(sorted(word_freq.items()))

    return sorted_word_freq

if __name__ == "__main__":
    # Take input text from the user
    input_text = input("Enter the text: ")

    # Compute word frequencies and sort the keys
    result = word_frequency(input_text)

    # Display the result
    print("\nWord Frequencies (sorted alphanumerically):")
    for word, freq in result.items():
        print(f"{word}: {freq}")
