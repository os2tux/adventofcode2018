import csv
import os 

def retrieve_frequencies(filepath):
    with open(filepath, 'r') as frequencies:
        reader = csv.reader(frequencies)
        file_contents = list(reader)

    freq_list = []
    for frequency in file_contents:
       freq_list.append(int(frequency[0]))

    return freq_list

def sum_total_frequency_changes(frequencies):
    print(sum(frequencies))

if __name__ == "__main__":
    filepath = os.getenv("AOC_INPUT_FILE")

    sum_total_frequency_changes(retrieve_frequencies(filepath))

