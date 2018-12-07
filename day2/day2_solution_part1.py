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

#This solution assumes that there are three states in which a string can exist, based on the
#the problem statement. It can either have nothing, duplicates, or triplicates. If 
#triplicates or duplicates exist, we must process the data differently. The first i
#component of our function inspects the string to determine what its state is. Once this 
#state is known, we then evaluate that state to determine how we should process the string
#(to which destination it should be sent). Because each state need only occur once for the 
#string classification process, we can assume that ANY existence of a given attribute is 
#enough to classify the string. Thus in the second component of the function, we evaluate 
#the attributes of each string individually to determine the state of its duplicates, and 
#process it accordingly 
def find_counts():
    box_ids = retrieve_boxIDs(filepath)
    ccounts = []
    twcount = []
    trcount = []

#Here we inspect the string to determine what duplicates or triplicates it has, if any, and
#store it for later processing. We don't do anything here other than evaluate the state of
#the string and store it 
    for boxid in box_ids:
        char_count = {}
        inspection = {boxid : char_count}
        
        for c in boxid:
            char_count[c] = boxid.count(c)
        
        ccounts.append(inspection)

#Here we can assume that if a string has both a duplicate and a triplicate value, it needs
#to be sent to both destinations. Else if it only has a duplicate, it need only be sent to 
#one destination 
    for d in ccounts:
        for k in d:
            if 2 in d[k].values() and 3 in d[k].values():
                twcount.append(k)
                trcount.append(k)
            elif 2 in d[k].values():
                twcount.append(k)

    ans = len(twcount) * len(trcount)
    
    print(ans)

if __name__ == "__main__":
    filepath = os.getenv("AOC_INPUT_FILE")

    find_counts()
