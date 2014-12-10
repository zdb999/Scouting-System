#!/usr
import sys
import os
from sdaps.utils import opencv

# Use the following and local_run=True below to run without installing SDAPS
#sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '..'))

import sdaps
#sdaps.init(local_run=True)

os.system("rm -r ./Project")
os.system("sdaps ./Project setup_tex Test.tex")
os.system("sdaps ./Project add --convert ./Project/questionnaire.pdf")
os.system("sdaps ./Project recognize")
os.system("sdaps ./Project gui")
os.system("sdaps ./Project csv export")
os.system("cp ./Project/data_1.csv ./Output_Data.csv")




