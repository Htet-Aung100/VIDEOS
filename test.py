rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85".split(",")
a = []
for i in rainfall_mi:
    a.append(float(i))
num_rainy_months = 0
for u in a:
    if u > 3.0:
        num_rainy_months+=1
print(num_rainy_months)

a = 1.23577
print("This is rainint in Nework")
print("First action")
print('the value of a is %.3f'%a)

