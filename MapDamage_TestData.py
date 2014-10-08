import random
import infra01_pos2info as in01


reads_count = 500000
chr_len = 249250000
freq = [0.4, 0.1, 0.05, 0.04, 0.03, 0.02, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.1, 0.4]
counts = {"+":{"c":[0]*100,"c_t":[0]*100},"-":{"c":[0]*100,"c_t":[0]*100}}


for i in range(0,reads_count):
  pos = int(random.random()*chr_len)
  seq = in01.get_seq_hg_mmap("chr1",pos,end+99)
  if i%2==0:
    strand = "+"
  else:
    strand = "-"
  
  

