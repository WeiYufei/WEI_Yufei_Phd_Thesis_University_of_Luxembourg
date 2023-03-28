import math
import numpy as np

P5R2 = 10**(0.1490 + 0.2728*5 + (0.000012152 -0.0000025368* 5)*100)
P5R27 = 10**(0.1490 + 0.2728*5 + (0.000012152 -0.0000025368* 5)*500)
P5R3 = 10**(0.1490 + 0.2728*5 + (0.000012152 -0.0000025368* 5)*1000)
P5R37 = 10**(0.1490 + 0.2728*5 + (0.000012152 -0.0000025368* 5)*5000)
P5R4 = 10**(0.1490 + 0.2728*5 + (0.000012152 -0.0000025368* 5)*10000)
 
print(np.round(P5R2,4))
print(np.round(P5R27,4))
print(np.round(P5R3,4))
print(np.round(P5R37,4))
print(np.round(P5R4,4))

print(np.round((P5R2-P5R27)/P5R2*100,4).real)
print(np.round((P5R27-P5R3)/P5R27*100,4))
print(np.round((P5R3-P5R37)/P5R3*100,4))
print(np.round((P5R37-P5R4)/P5R37*100,4))

print('%%%%%')
P6R2 = 10**(0.1490 + 0.2728*6 + (0.000012152 -0.0000025368* 6)*100)
P6R27 = 10**(0.1490 + 0.2728*6 + (0.000012152 -0.0000025368* 6)*500)
P6R3 = 10**(0.1490 + 0.2728*6 + (0.000012152 -0.0000025368* 6)*1000)
P6R37 = 10**(0.1490 + 0.2728*6 + (0.000012152 -0.0000025368* 6)*5000)
P6R4 = 10**(0.1490 + 0.27280*6 + (0.000012152 -0.0000025368* 6)*10000)
 
print(np.round(P6R2,4).real)
print(np.round(P6R27,4).real)
print(np.round(P6R3,4).real)
print(np.round(P6R37,4).real)
print(np.round(P6R4,4).real)


print(np.round((P6R2-P6R27)/P5R2*100,4).real)
print(np.round((P6R27-P6R3)/P5R27*100,4).real)
print(np.round((P6R3-P6R37)/P5R3*100,4).real)
print(np.round((P6R37-P6R4)/P5R37*100,4).real)
print('%%%%%')

P7R2 = 10**(0.1490 + 0.2728*7 + (0.000012152 -0.0000025368* 7)*100)
P7R27 = 10**(0.1490 + 0.2728*7 + (0.000012152 -0.0000025368* 7)*500)
P7R3 = 10**(0.1490 + 0.2728*7 + (0.000012152 -0.0000025368* 7)*1000)
P7R37 = 10**(0.1490 + 0.2728*7 + (0.000012152 -0.0000025368* 7)*5000)
P7R4 = 10**(0.1490 + 0.2728*7 + (0.000012152 -0.0000025368* 7)*10000)
 
print(np.round(P7R2,4).real)
print(np.round(P7R27,4).real)
print(np.round(P7R3,4).real)
print(np.round(P7R37,4).real)
print(np.round(P7R4,4).real)

print(np.round((P7R2-P6R27)/P7R2*100,4).real)
print(np.round((P7R27-P6R3)/P7R27*100,4).real)
print(np.round((P7R3-P6R37)/P7R3*100,4).real)
print(np.round((P7R37-P6R4)/P7R37*100,4).real)
