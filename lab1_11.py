a = [1,2,12,4];
b = [2,4,2,8];
sum = 0;
for index in range(len(a)):
    sum = sum + a[index]*b[index];
print('Iloczyn skalarny wynosi: '+str(sum));