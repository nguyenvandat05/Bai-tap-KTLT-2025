## My script using the math module ## 
print("Nguyen Van Dat")
print("MSSV:235752020710019")
import mymath  # Note no .py 
values = [2,4,6,8,10] 
print('Squares:') 
for v in values: 
    print(mymath.square(v)) 
print ('Cubes:')
for v in values: 
    print(mymath.cube(v)) 
print('Average: ' + str(mymath.average(values)))
