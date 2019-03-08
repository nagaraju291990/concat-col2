#Program to read a file(tab seperated) and if column1 is repeated more than once its corresponding column2 is appended with existing one
#for ex srcTABtgt1 srcTABtgt2=> srcTABtgt1, tgt2

#!/usr/bin/python3
import re
import sys

#read file
file=open(sys.argv[1],"r+")


#dictionary to save column1 as keys and column2 as values
dict={}

for line in file.read().split("\n"):
#split("\n") will split according to newline
    #print (line)

    if(line == ""):
        break

    #cleaning corpus
    #line = line.lower() #convert to lowercase
    line = re.sub(r'\u00A0'," ",line,flags=re.MULTILINE)
    line = re.sub(r'^ *',"",line,flags=re.MULTILINE)
    line = re.sub(r' *$',"",line,flags=re.MULTILINE)
    line = re.sub(r' +', " ",line,flags=re.MULTILINE)
    line = line.lstrip()

    col1_col2 = line.split("\t")

    col1 = col1_col2[0]
    col2 = col1_col2[1]

    #check if col1 already exists in dictionary
    if col1 not in dict:
        dict[col1] = col2
    else:
        tmp = dict[col1]
        tmp2 = tmp + "," + col2
        tmp2 = re.sub(r' ?, ?', ',', tmp2)
        my_list = tmp2.split(",")
        my_list = list(set(my_list))
        dict[col1] = ', '.join(my_list)
        #print(line)


#print the dictionary with keys and values
#for k,v in wordcount.items():
    #print (k, v)

#print the dictionary with sorted keys(tokens) and values
for k in sorted(dict):
    print (k, dict[k],sep='\t')
