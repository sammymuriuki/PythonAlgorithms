''' Convert tuple into a dictionary '''
tuple1 = (('make','toyota'), ('model','landcruiser'), ('YOM','2019'), ('color','black'));
dict1 = dict();
for x, y in tuple1:
    dict1.setdefault(x, []).append(y);

print(dict1);

''' Method 2 '''
tuple2 = (('make','toyota'), ('model','landcruiser'), ('YOM','2019'), ('color','black'));
dict2 = dict(tuple2);
print(dict2);
