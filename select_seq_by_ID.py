# Python script to recover sequences from a fasta file from a list of IDs.
# Run the script as following: python select_seq_by_ID.py <fasta file> <ID file> <output file>

import sys
header = []
sequence = []
count = -1
file_open = open(sys.argv[1],"r") #fasta file to be analyzed
for line in file_open:
    line = line.rstrip()
    if ">" in line:
        temp=line.split(" ")
        header.append(temp[0])
    
        count+=1
        sequence.insert(count,'')
    else:
        sequence[count]+=line
con=count+1

print ("The number of sequences in this file is:") #for checking
print (con)
result=""
file3 = open(sys.argv[2], "r") #file contianing the IDs of sequences, one per line
file4 = open(sys.argv[3], "w") # output file

for line in file3: 
    line=line.rstrip()
    
    for i in range (count):
        if (line in header[i]) & (len(line) == len(header[i])-1):
            result=str(header[i])+"\n"+  str(sequence[i]) + "\n"
            file4.write(str(result))     