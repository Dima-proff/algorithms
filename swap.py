x,y = 10,20

#tuple's method

x, y = y, x

#under the hood tuple's method

tmp1 = x
tmp2 = y

x = tmp2
y = tmp1

#bitwise XOR (binary operation)

x = x ^ y
y = x ^ y
x = x ^ y