"""
script to reformat the occupation code and their titles into a dataframe
and save as csv
"""

import pandas as pd
import io
import sys
import getopt


def reformat(path):
   with open(path, 'r') as f:
    data = f.read().replace('\n    ', ';')

    df = pd.read_csv(io.StringIO(data), sep=';', header=None)   
    df.columns = ['Code', 'occupation']

    df.to_csv(path, index=False, sep=';')


def main(argv):
   file = ''
   opts, args = getopt.getopt(argv,"hp:",["file="])
   for opt, arg in opts:
      if opt == '-h':
         print ('occ_codes.py -p <filepath>')
         sys.exit()
      elif opt == '-p':
        file = arg
        reformat(file)


if __name__ == "__main__":
   main(sys.argv[1:])