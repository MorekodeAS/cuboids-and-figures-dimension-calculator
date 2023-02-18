import math
first_name = input('Hello! What`s your name?')
print('Hello ' + first_name)
print('We need dimensions our cuboid. Please describe')
dimensionX = float(input('lenght: '))
dimensionY = float(input('high: '))
dimensionZ = float(input('deep: '))
if dimensionZ > 0 and dimensionY > 0 and dimensionX > 0:
    sum_of_area = dimensionX * dimensionY + dimensionX * dimensionZ + dimensionZ * dimensionY
    print(f'surface area = {sum_of_area * 2}')
    print(f'volume: {dimensionX * dimensionY * dimensionZ}')
    diagonal_of_figure = (math. sqrt(dimensionX **2 + dimensionY ** 2))
    print(f'diagonal of cuboid = {math. sqrt(diagonal_of_figure ** 2 + dimensionZ ** 2)}')
else :
    print('All dimensions have to be higher than 0')
