import re
import sys
from datetime import datetime

start_time = datetime.now() # track execution time
class Vcf:
  def __init__(self, file_name):
    self.file_name = file_name

  def vcfParse(self):
    metadata = [] # list to store metadata
    file_names = {} # capture file names to manage file handlers
    
    with open(self.file_name) as file:
        for line in file: # loop through each line of input vcf file
            line = line.rstrip()
            if line.startswith("##"): # process metadata
                metadata.append(line)
            elif line.startswith("#CHROM"): # process header columns
                header_line = re.split(r"\t+", line)
                num_columns = len(header_line)
            else:
                for sample_num in range(9, num_columns): # loop through samples and write to output 
                    sample_name = header_line[sample_num]
                    if sample_name not in file_names: # open file handle only for unprocessed samples
                        file_names[sample_name] =  open(sample_name + '.vcf', 'w')
                        file_names[sample_name].write("\n".join(metadata) + "\n" + "\t".join(header_line[0:9]) + "\t" + sample_name + "\n")
                    
                    split_line = re.split(r"\t+", line)
                    file_names[sample_name].write("\t".join(split_line[0:9]) + "\t" + split_line[sample_num] + "\n")
                    
    for key in file_names: # close file handles
        file_names[key].close()

vcf_file = sys.argv[1]
vcf = Vcf(vcf_file)
vcf.vcfParse()

print("Execution time -----> " + str(datetime.now() - start_time))