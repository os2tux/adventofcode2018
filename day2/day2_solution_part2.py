import csv
import os 

def retrieve_boxIDs(filepath):
    with open(filepath, 'r') as boxIDs:
        reader = csv.reader(boxIDs)
        file_contents = list(reader)

    boxID_list = []
    for boxID in file_contents:
       boxID_list.append(boxID[0])

    return boxID_list


if __name__ == "__main__":
    filepath = os.getenv("AOC_INPUT_FILE")

    find_counts()
