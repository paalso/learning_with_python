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
from vectors import dot_product, sub_vectors, scalar_mult

def main():
    a = [3, 4, 5, 0]
    b = [-5, 5, 10, 1]
    c = [10, 1, 1, 5]

	# 285
    print (dot_product(sub_vectors(scalar_mult(5, a), scalar_mult(3, b)), c))


if __name__ == '__main__':
    main()
