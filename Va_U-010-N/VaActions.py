from VaDirectionDetector import getDirection
from VaData import VaData

### Action__start ###################################################
def Action__start(va_data, local_data):
    print('Action__start')


    return getDirection(va_data, local_data)

### Action__add_to_sum ###################################################
def Action__add_to_sum(va_data, local_data):
    print('Action__add_to_sum')

    local_data.set('The sum of elements of array...sum', 
    local_data.get('The sum of elements of array...sum') + local_data.get('The current element of array M...current element'))


    return getDirection(va_data, local_data)

### Action__do_nothing ###################################################
def Action__do_nothing(va_data, local_data):
    print('Action__do_nothing')


    return getDirection(va_data, local_data)

### Action__met_array ###################################################
def Action__met_array(va_data, local_data):

    """
    va_data['d_level_desc']['v'] = {
    "d_level_type":"list", 
    "d_index":0, 
    "d_max_index":len(va_data['current_element']['v']) - 1
    }

    """

    local_data.set('The depth level description...d_level_description_obj', VaData())
    local_data.get('The depth level description...d_level_description_obj').set("The depth level...d_level_type","list")
    local_data.get('The depth level description...d_level_description_obj').set("The depth level index...d_index", 0)
    local_data.get('The depth level description...d_level_description_obj').set("The depth level max index...d_max_index",
                        len(local_data.get('The current element of array M...current element')) - 1)


    #va_data['d_level_stack']['v'].append(va_data['d_level_desc']['v'])
    temp_d_level_stack = local_data.get('The depth level stack array...d_level_stack')
    temp_d_level_stack.append(local_data.get('The depth level description...d_level_description_obj'))
    local_data.set('The depth level stack array...d_level_stack',temp_d_level_stack)

    #va_data['d_level_stack_pointer']['v'] = 0
    local_data.set('The depth level stack pointer...d_level_stack_pointer', 0)



    return getDirection(va_data, local_data)

### Action_9000 ###################################################
def Action_9000(va_data, local_data):
    print('Action_9000')


    return getDirection(va_data, local_data)
