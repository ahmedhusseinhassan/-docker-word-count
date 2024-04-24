import nltk
from nltk.corpus import stopwords
from collections import Counter
# Download NLTK data (run once)
nltk.download('stopwords')
nltk.download('punkt')
# Function to read file, remove stop words, and count word frequencies
def word_frequency_analysis(file_path):
    # Read file
    with open(file_path, 'r') as file:
        text = file.read().lower()

    # Tokenize words
    words = nltk.word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Count word frequencies
    word_freq = Counter(filtered_words)

    return word_freq

if __name__ == "__main__":
    file_path = "/app/paragraphs.txt"
    word_freq = word_frequency_analysis(file_path)

    # Display word frequency count
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")
