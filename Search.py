#!/usr
import sys
import os
from sdaps.utils import opencv
import time
import csv

# Use the following and local_run=True below to run without installing SDAPS
#sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '..'))

import sdaps
#sdaps.init(local_run=True)

File_List = []
count = 0
cycle = 0
G_id_list = []
Acceptable = ["001","034"]
c2 = 0

while cycle < 30:

 File_List = os.listdir("./Scans")
 N_Files = len(File_List)

 if N_Files > 0:

  os.system("cp -r ./Base ./Conversion")

  for count in range(len(File_List)):
     file_ending = File_List[count].split(".")
     os.system("sdaps ./Conversion add --convert ./Scans/" + File_List[count])
     os.system("mv ./Scans/" + File_List[count] + " ./Archive/" + str(len(os.listdir("./Archive")) + 1) + "." + file_ending[1])

  os.system("sdaps ./Conversion recognize --identify")
  os.system("sdaps ./Conversion csv export")

  with open('./Conversion/data_1.csv', 'rb') as csvfile:
         Data = csv.reader(csvfile, delimiter=',', quotechar='|')
         for row in Data:
           G_id_list.append(row[1])
  csvfile.close

  for c2 in range(len(File_List)):

    if G_id_list[c2+1] not in Acceptable:
         G_id_list[c2+1] = "Unknown"
    os.system("mv ./Conversion/" + str(c2+1) + ".tif ./Converted_" + G_id_list[c2+1] + "/" + str(len(os.listdir("./Converted_" + G_id_list[c2+1])) + 1) + ".tif")

  os.system("rm -r ./Conversion")

 else:
  time.sleep(2)
  cycle = cycle + 1

print "Finished"

