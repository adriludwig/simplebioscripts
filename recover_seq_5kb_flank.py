# Python script to recover sequences from a fasta file from blast result.
# The sequences will be recovered with 5 kb of flanking regions
# Run the script as following: python recover_seq_5kb_flank.py <fasta file> <blast result file> <output file>
import sys
header = []
sequence = []
count = -1
file_open = open(sys.argv[1],"r") #fasta file to be analyzed
for line in file_open:
    line = line.rstrip()
    if ">" in line:
        header.append(line)
        count+=1
        sequence.insert(count,'')
    else:
        sequence[count]+=line
con=count+1
print ("The number of sequences in this file is:") #for checking
print (con)
region=''
nucleotide=''
ini=''
fin=''
result=''
file3 = open(sys.argv[2], "r") #file containing the tabular result of blast 
file4 = open(sys.argv[3], "w") # output file
for line in file3: 
    line=line.rstrip()
    temp = line.split("\t")
    if int(temp[8])<=int(temp[9]):
       inicial = int(temp[8])
       final = int(temp[9])
    else:
        inicial= int(temp[9])
        final = int(temp[8])
    if inicial <= 5000: #change here if you want to change the flanking region size
        inicial2 = 1
        final2 = final +5000 #change here if you want to change the flanking region size
    else:
        inicial2 = inicial - 5000 #change here if you want to change the flanking region size
        final2 = final + 5000 #change here if you want to change the flanking region size
       
        
    for i in range (con):
        if temp[1] in header[i]:
            if (temp[8]<temp[9]):
                ini=int(inicial2)
                fin= int(final2)
                nucleotide = sequence[i]
                region = nucleotide[int(ini):int(fin)]
                result = ">"+ str(temp[1]) +"_" + str(ini)+ "_" + str(fin)+"\n"+str(region)+"\n"
            else:
                ini=int(inicial2)
                fin= int(final2)
                nucleotide = sequence[i]
                region = nucleotide[int(ini):int(fin)]
                region=region.upper()
                region=region.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
                region=region[::-1]
                result = ">"+ str(temp[1]) + "_" + str(ini)+ "_" + str(fin)+"\n"+str(region)+"\n"     
    file4.write(str(result))        