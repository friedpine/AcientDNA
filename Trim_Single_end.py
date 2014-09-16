#!/usr/bin/python
import re,sys,gzip

def remove_low_quantity(seq,qua):
  pos = re.search("#*?$",qua).start()
  return seq[0:pos],qua[0:pos]
  
def reverse_complementary(seq):
  comp = {"A":"T","T":"A","C":"G","G":"C","N":"N"}
  RC_seq = ""
  for i in seq:
    RC_seq += comp[i]
  return RC_seq[::-1]
  
def adaptor_pair1_pos(seq):
  pos = [-1]
  try:
    pos.append(re.search("AGATCGGAAGA",seq).start())
    pos.append(re.search("GCACACGTCTG",seq).start()-11)
    pos.append(re.search("GGAAGAGCACA",seq).start()-5)
  except:
    tmp = 1
  return pos

def pairs_merge_by_adaptor(seq1,seq2,qua1,qua2):
  seq1,qua1 = remove_low_quantity(seq1,qua1)
  adp_pos_1 = adaptor_pair1_pos(seq1)
  adp_pos = max(adp_pos_1)
  if adp_pos > 0:
    return 1,seq1[0:adp_pos],qua1[0:adp_pos]
  else:
    return 0,"NA","NA"
  
fq1 = gzip.open(sys.argv[1],'rb')

out = open("merged.txt","wb")

total = 0
adaptor = 0

while 1:
  head1 = fq1.readline()
  if head1 == '':
    break
  seq1 = fq1.readline()
  tmp = fq1.readline()
  qua1 = fq1.readline()
  total += 1
  state,seq,qua = pairs_merge_by_adaptor(seq1,qua1)
  if state == 1:
    adaptor += 1
    if len(seq)>=25:
    	out.write(head1+seq+"\n+\n"+qua+"\n")
out.close()
print total,adaptor