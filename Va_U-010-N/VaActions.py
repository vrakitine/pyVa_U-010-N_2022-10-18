from VaDirectionDetector import getDirection

### Action_000 ###################################################
def Action_000(va_data):
    print('Action_000')
 
    va_data['sum_01'] = {}
    va_data['sum_01']['d'] = "The sum of elements of array"
    va_data['sum_01']['v'] = 0

    va_data['i_main'] = {}
    va_data['i_main']['d'] = "The index in the all array" 
    va_data['i_main']['v'] = -1

    va_data['current_element'] = {}
    va_data['current_element']['d'] = "It is element of array, the v-agent is working with in this time in the current Action_xxx"
    va_data['current_element']['v'] = 'Unknown'

    va_data['custom_log'] = {}
    va_data['custom_log']['d'] = "This is the log array for tracking custom variables in actions."
    va_data['custom_log']['v'] = [] 

    """
    va_data[''] = {}
    va_data['']['v'] = 0
    va_data['']['d'] = "Empty"
    """
    ### End | Init setting

    ### for log
    va_data['custom_log']['v'].append('i_main')
    va_data['custom_log']['v'].append('current_element')
    va_data['custom_log']['v'].append('sum_01')

    return getDirection(va_data)


    return va_data

### Action_010 ###################################################
def Action_010(va_data):
    print('Action_010')

    va_data['sum_01']['v'] += va_data['current_element']['v']

    ### for log 
    va_data['custom_log']['v'].append('i_main')
    va_data['custom_log']['v'].append('current_element')
    va_data['custom_log']['v'].append('sum_01')

    return getDirection(va_data)


### Action_020 ###################################################
def Action_020(va_data):
    print('Action_020')

    ### for log
    va_data['custom_log']['v'].append('i_main')
    va_data['custom_log']['v'].append('current_element')
    va_data['custom_log']['v'].append('sum_01')

    return getDirection(va_data)

### Action_9000 ###################################################
def Action_9000(va_data):
    print('Action_9000')

    return getDirection(va_data)