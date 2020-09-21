
import sys
import math

# tetration function
# if not converge, output INFINITY!
# f = X^X^X^X.....
EPSILON = 1e-5

c= float(sys.argv[1])
base = c
t = c
old = t - 10
while abs(old - t) > EPSILON :
    if t//old > 10:
        print('INFINITY! NOT CONVERGE!')
        break
    old = t
    t = math.pow(base, t)
    print(t)
print(t)

#1.4   ->1.8867
#1.5   NOT CONVERGE
#0.01  NOT CONVERGE
#0.08  ->0.3815..
