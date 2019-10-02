#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      PaulS
#
# Created:     06.08.2019
# Copyright:   (c) PaulS 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from vectors import *

def main():
    a = [4, -3, 4]
    b = [2, 4, -2]
    c = [4, 3, 4]

    print(det3(a,b,c))

if __name__ == '__main__':
    main()
