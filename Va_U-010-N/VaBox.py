from VaActions import *
from VaDirectionDetector import *
from VaBoxTools import *


def start(va_data):

    va_data = Action_000(va_data)
  
    while 1 == 1: 
      va_data['va']['v']['jump']['v'] += 1
      if va_data['va']['v']['jump']['v'] > va_data['va']['v']['max_jump']['v']:
        print(va_data)
        print("\n\n Error: Looping")
        break

      temp = va_data['va']['v']['script']['v'][va_data['va']['v']['current_action']['v']][va_data['va']['v']['direction']['v']]

      va_data['va']['v']['previous_action']['v'] = va_data['va']['v']['current_action']['v']
      va_data['va']['v']['current_action']['v'] = temp  

      
    print('The v-agent is finished jumping in the action [', va_data['va']['v']['current_action']['v'], ']')    

    return