# coding: utf-8

import sys, io, os,codecs
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


sys.stdout = codecs.EncodedFile(sys.stdout, 'utf-8')  #sapporo
#sys.stdout = codecs.getwriter('utf_8')(sys.stdout)   #apricot

### Constants

ROOT = os.path.abspath(os.path.dirname(__file__))

EOU="SYMEOU"
EOS="SYMEOS"
SYMUNK="SYMUNK"
SYMREP="SYMREP"

#色付き文字
#BLUE = '\033[94m'
#GREEN = '\033[92m'
#YELLOW = '\033[93m'
#RED = '\033[91m'

BOLD= '\033[1m'
UNDERLINE= '\033[4m'
BLACK= '\033[30m'
BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
ENDC = '\033[0m'
