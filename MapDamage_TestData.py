import os, sys, re
sys.path.insert(0,'/datc/fanxiaoying/git/BioModule')
import random
import infra01_pos2info as in01

reads_count = 10000
chr_len = 249250000
freq = [0.4, 0.1, 0.05, 0.04, 0.03, 0.02, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.1, 0.4]
out = open("mapdamage_test_data.fq","wb")

counts = {"+":{"c":[0]*100,"c_t":[0]*100},"-":{"c":[0]*100,"c_t":[0]*100}}
total = [0,0]

for i in range(0,reads_count):
  pos = int(random.random()*chr_len)
  seq = in01.get_seq_hg_mmap("chr1",pos,end+99)
  if N in seq:
    continue
    if i%2==0:
      strand = "+"
      total[0] += 1
    else:
      strand = "-"
      total[1] += 1
  for index,base in enumerate(seq):
      if base == "C":
        counts[strand]["c"][index] += 1
        if random.random()<freq[index]:
          seq[index] = "T"
          counts[strand]["c_t"][index] += 1
  if strand == "-":
    seq = in01.reverse_complementary(seq):
  out.write(">TEST"+pos+"_"+i+"\n+seq+"\n")
  
print total  
print counts
  
  

