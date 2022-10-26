
import VaBox
import VaActions
import VaBoxTools
import VaScript
import VaConfigLocal

va_data = {}

va_data = VA_config.setup(va_data)

"""
va_data['va']['v']['is_tracking_on'] = {}
va_data['va']['v']['is_tracking_on']['v'] = False
va_data['va']['v']['is_tracking_on']['d'] = "Is tracking ON? (True/False)"


va_data['va']['v']['tracking_actions'] = {}
va_data['va']['v']['tracking_actions']['v'] = ['Action_010']
va_data['va']['v']['tracking_actions']['d'] = "The list of actions to track"
    
va_data['va']['v']['jump_pause_after_actions'] = {}
va_data['va']['v']['jump_pause_after_actions']['v'] = ['Action_010']
va_data['va']['v']['jump_pause_after_actions']['d'] = "The jump pause after actions"
"""

va_data['M'] = {}
va_data['M']['d'] = "Input array"
va_data['M']['v'] = [10,-20, 1.3, 5, 7, 15]
va_data['M']['v'] = [2,-3, 1, 5]
#va_data['M']['v'] = [5]


print(va_data['M'])

va_data = VA_box.start(va_data)

print(va_data['sum_01'])

VA_box_tools.VA_print_direction_action_tracking(va_data)

print('\nThe end')
