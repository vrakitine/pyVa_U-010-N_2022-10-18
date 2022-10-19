from VA_actions import *
from VA_direction_detector import *
from VA_box_tools import *


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

      if va_data['va']['v']['is_tracking_on']['v'] and (va_data['va']['v']['previous_action']['v'] in va_data['va']['v']['tracking_actions']['v']):
        va_data = VA_tracking_row(va_data)
        va_data = VA_set_direction_action_tracking(va_data)
        va_data = Action_variables_tracking_row(va_data)
        print("\n")
      
      if va_data['va']['v']['current_action']['v'] in va_data['va']['v']['script']['v']:
        if va_data['va']['v']['current_action']['v'] in va_data['va']['v']['jump_pause_after_actions']['v'] and va_data['va']['v']['is_tracking_on']['v'] and (va_data['va']['v']['current_action']['v'] in va_data['va']['v']['tracking_actions']['v']):
          print("jump_pause_after_actions:", va_data['va']['v']['jump_pause_after_actions']['v'])
          temp = input("pause ===> after action:[" + va_data['va']['v']['current_action']['v'] + "] <enter> - continue, <space><enter> - break")
          if temp == ' ':
            break
        va_data['va']['v']['direction']['v'] = 'direction unknown'        
        eval(va_data['va']['v']['current_action']['v'] + "(va_data)")
      else:
        break

    print('The v-agent is finished jumping in the action [', va_data['va']['v']['current_action']['v'], ']')    

    return va_data

def Action_variables_tracking_row(va_data):
    print(">>> custom_log -->")
    if len(va_data['custom_log']['v']) == 0:
        print("\tEmpty")
    for temp in va_data['custom_log']['v']:
        print("\t" + temp ,"= [" + str(va_data[temp]['v']) + "] <-- " +  va_data[temp]['d'])
    va_data['custom_log']['v'] = []

    return va_data 