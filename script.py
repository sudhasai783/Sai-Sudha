import os
from collections import Counter
import socket

# Function to count words in a text file
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

# Function to find top N words with counts in a text file
def top_words(filename, N=3):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        word_counts = Counter(words)
        return word_counts.most_common(N)

# List all text files in the /home/data directory
files = os.listdir('/home/data')

# Count total number of words in each text file
total_words = sum(count_words('/home/data/' + file) for file in files)

# Find top 3 words with counts in IF.txt
top_words_if = top_words('/home/data/IF.txt')

# Find the IP address of the machine
ip_address = socket.gethostbyname(socket.gethostname())

# Write the output to result.txt
with open('/home/output/result.txt', 'w') as result_file:
    result_file.write(f"List of text files: {', '.join(files)}\n")
    result_file.write(f"Total number of words in both files: {total_words}\n")
    result_file.write("Top 3 words with counts in IF.txt:\n")
    for word, count in top_words_if:
        result_file.write(f"{word}: {count}\n")
    result_file.write(f"IP address of the machine: {ip_address}\n")

# Print the output to console
with open('/home/output/result.txt', 'r') as result_file:
    print(result_file.read())
