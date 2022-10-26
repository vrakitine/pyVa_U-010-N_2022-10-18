import VaBox
import VaActions
import VaBoxTools
import VaScript
import VaConfig
import VaConfigLocal
from VaData import VaData


va_data = VaData()
VaConfig.setup(va_data)
local_data = VaData()
VaConfigLocal.setup(local_data)

test = va_data.getAll()
print(test)
print('------------------------')
test = local_data.getAll()
print(test)
print('------------------------')
#VaBox.start(va_data,local_data)


print('\nThe end')

