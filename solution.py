import re

metadata = [] # list to store metadata
file_names = {} # capture file names to manage file handlers

with open("test_1.vcf") as file:
    
    for line in file: # loop through each line of input vcf file
        line = line.rstrip()
        if line.startswith("##"):
            metadata.append(line)
        elif line.startswith("#CHROM"):
            header_line = re.split(r"\t+", line)
            num_columns = len(header_line)
            
        else:
            for i in range(9, num_columns): 
                if header_line[i] not in file_names:
                    file_names[header_line[i]] =  open(header_line[i] + '.vcf', 'w')
                    file_names[header_line[i]].write("\n".join(metadata) + "\n" + "\t".join(header_line[0:8]) + "\t" + header_line[i] + "\n")
                  
                split_line = re.split(r"\t+", line)
                file_names[header_line[i]].write("\t".join(split_line[0:8]) + "\t" + split_line[i] + "\n")
                
    for key in file_names:            
        file_names[key].close()