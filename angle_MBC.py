
from math import radians
from math import pi
from math import degrees


ab_length = int(input())
bc_length = int(input())

ac_length = round(pow(pow(ab_length, 2) + pow(bc_length,2), 0.5))
mc_length = ac_length / 2 
mb_length = round(pow(pow(bc_length, 2) - pow(mc_length,2), 0.5))
sin_radians = mc_length / bc_length
sin_degree =  degrees(sin_radians)

print(f"{sin_degree}°")
