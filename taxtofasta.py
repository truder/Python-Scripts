#!/usr/bin/env python

#rm import os
#import numpy
#import argparse
#import sys
#import csv
#import time
import subprocess
import datetime
from optparse import OptionParser

parser = OptionParser("\n\n %prog [options]")
parser.add_option('-t', '--tpath', type="string", dest = 'tpath', help="Path to Taxonomy file")
parser.add_option('-f', '--fpath', type='string', dest='fpath', help="Path to Fasta file")
parser.add_option('-w', '--wpath', type='string', dest='wpath', help="Path to Write file")
(opts, args) = parser.parse_args()
#tpath = "/srv/whitlam/bio/db/gg/qiime_gg_2012/gg_12_10_otus/taxonomy/97_otu_taxonomy.txt"
#fpath = "/srv/whitlam/bio/db/sequenceserver/blastdb/greengenes_97_2012.fna"

#tpath = "/srv/whitlam/bio/db/Silva/QIIME_files_r108/taxa_mapping/Silva_108_taxa_mapping.txt"
#fpath = "/srv/whitlam/bio/db/sequenceserver/blastdb/Silva_108_rep_set.fna"

#wpath = "/srv/whitlam/home/users/uqtruder/scripts/taxtofasta/20130617taxgg_97_2012.fna"

#tpath = "/srv/whitlam/home/users/uqtruder/scripts/taxhead.txt"
#fpath = "/srv/whitlam/home/users/uqtruder/scripts/fastasample.fna"
#wpath = "/srv/whitlam/home/users/uqtruder/scripts/taxfasta.fna"
tpath = opts.tpath
fpath=opts.fpath
wpath=opts.wpath

#Hash Taxonomy File
print "TAXONOMY ..."
hashlib = {}
t1 = open(tpath, 'rU')
for t2 in t1:
  t3 = t2.split('\t')
  taxid = t3 [0]
  taxstring = t3 [1]
  hashlib[taxid] = taxstring

#Evaluate fasta File based on Hashed Taxonomy file
print "FASTA ..."
f1 = open(fpath, 'rU')
taxfasta = open(wpath, 'w+')
for f2 in f1:
  f3 = f2.strip()
  if f3.startswith('>'):
    f4 = f3.replace(">", "")
    f5 = f4.strip()
    taxfasta.write('>')
    taxfasta.write(f5)
    taxfasta.write(' ')
    taxfasta.write(hashlib[f4])
  else:
    taxfasta.write(f2)
taxfasta.close()

#Write a logfile

date = datetime.datetime.now()
lpath = "logfile_taxtofastamk5.txt"
logfile=open(lpath, 'a+')
logfile.write(str(date))
logfile.write('\n')
logfile.write("Taxonomy File: ")
logfile.write(tpath)
logfile.write('\n')
logfile.write("Fasta File: ")
logfile.write(fpath)
logfile.write('\n')
logfile.write("Output File: ")
logfile.write(wpath)
logfile.write('\n')

#run seqmagick and return output/write to logfile
print"CHECKING ..."
seqmagick=subprocess.Popen(['seqmagick', 'info', fpath, wpath], stdout=subprocess.PIPE)
for l in seqmagick.stdout:
  print l
  logfile.write(l)
logfile.write('\n\n')
logfile.close()

print "DONE"





