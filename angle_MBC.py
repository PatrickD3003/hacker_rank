# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import degrees
from math import atan

ab_length = int(input())
bc_length = int(input())

tan_radians = atan(ab_length / bc_length)
sin_degree =  round(degrees(tan_radians))
degree_sign = u"\N{DEGREE SIGN}"
print(f"{sin_degree}{degree_sign}")

