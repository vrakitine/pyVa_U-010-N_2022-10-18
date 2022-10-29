import VaBox
import VaActions
import VaScript
import VaConfig
import VaConfigLocal
from VaData import VaData


va_data = VaData()
VaConfig.setup(va_data)
local_data = VaData()
VaConfigLocal.setup(local_data)

local_data.set('Input array...M', [5, 6 , 3])


test = va_data.getAll()
#print(test)
print('------------------------')
test = local_data.getAll()
print(test)
print('------------------------')
test = local_data.get('The depth level description...d_level_description_obj')
test = test.getAll()
print(test)
print('------------------------')
print(local_data.getNameValue('Input array...M'))
print('------------------------')
VaBox.start(va_data,local_data)

print(local_data.getNameValue('The sum of elements of array...sum'))

print('\nThe end')

