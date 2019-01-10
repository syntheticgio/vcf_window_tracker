#!/usr/bin/python

import pyvcf
import argparse
import pysam
import csv
# import _thread
# import threading

WINDOW_SIZE = 10000
CHROMOSOMES = [249250621, 243199373, 198022430, 191154276, 180915260, 171115067, 159138663, 146364022, 141213431, 135534747, 135006516, 133851895, 115169878, 107349540, 102531392, 90354753, 81195210, 78077248, 59128983, 63025520, 48129895, 51304566, 155270560, 59373566, 16571]
CHROMOSOME_NAMES = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X","Y","M"]

# class myThread (threading.Thread):
#    def __init__(self, threadID, name):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#    def run(self):
#       print ("Starting " + self.name)
#       create_windows(self.name)
#       print ("Exiting " + self.name)



def create_windows(vcf_data, output_file):
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    while open(output_file, 'w') as window_file:
        vcf_writer = csv.writer(window_file, delimiter=',')

        i = 0
        for chrom in CHROMOSOMES:
            # This should get the number of windows we should see
            _w = int(chrom / WINDOW_SIZE)

            for x in range(0 , _w):
                s = x * WINDOW_SIZE
                e = s + WINDOW_SIZE - 1
                window = vcf_data.fetch(CHROMOSOME_NAMES[i], start=s, end=e)
                hits = len(window) # This should be the number of hits in the region
                vcf_writer.writerow([CHROMOSOME_NAMES[i], s, e, hits])

            # get last bit of chromosome ..
            s = e + 1
            e = chrom - 1
            window = vcf_data.fetch(CHROMOSOME_NAMES[i], start=s, end=e)
            hits = len(window)
            vcf_writer.writerow([CHROMOSOME_NAMES[i], s, e, hits])
                
            i += 1
        
        # threadName.exit()

def main(vcf_list):
    i = 0
    for vcf in vcf_list:
        i += 1
        vcf_data = vcf.Reader(filename=vcf)

        # Create windows
        create_windows(vcf_data)
        # thread1 = myThread(i, "Thread-{}".format(i))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process VCF file.')
    parser.add_argument('--vcf', metavar='VCF_file', type=str, nargs='+',
                    help='vcf files to be parsed', action='append', 
                    dest='vcfs')
    

    args = parser.parse_args()
    main(args.vcfs)