import csv
import os 
import subprocess

sample_input = [1, -2, 3, 1]

#Opens and retrieves input
def retrieve_frequencies(filepath):
    with open(filepath, 'r') as frequencies:
        reader = csv.reader(frequencies)
        file_contents = list(reader)

    return file_contents

def compare_frequencies():
    freq = retrieve_frequencies(filepath)
    dups = False
    sums = {}
    vals = [0]

    while dups == False:
        for f in freq:
            #ans = vals[-1] + f
            ans = vals[-1] + int(f[0])
            vals.append(ans) 
            
            if ans in sums:
                print(ans)
                dups = True
                break
            else:
                sums[ans] = ""

if __name__ == "__main__":
    filepath = os.getenv("AOC_INPUT_FILE")
    compare_frequencies()
    
