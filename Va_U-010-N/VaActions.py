from VaDirectionDetector import getDirection

### Action_000 ###################################################
def Action_000(va_data, local_data):
    print('Action_000')



    return getDirection(va_data, local_data)

### Action_010 ###################################################
def Action_010(va_data, local_data):
    print('Action_010')
    #va_data['sum_01']['v'] += va_data['current_element']['v']
    local_data.set('The sum of elements of array...sum', 
    local_data.get('The sum of elements of array...sum') + local_data.get('The current element of array M...current element'))


    return getDirection(va_data, local_data)

### Action_020 ###################################################
def Action_020(va_data, local_data):
    print('Action_020')


    return getDirection(va_data, local_data)

### Action_9000 ###################################################
def Action_9000(va_data, local_data):
    print('Action_9000')


    return getDirection(va_data, local_data)
