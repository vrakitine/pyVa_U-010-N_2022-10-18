def getDirection(va_data, local_data):

    # In this function below we are determine the direction depending on the current element of the array.

    # "Direction_10"    -> "If the current element of the array > 0 and int and (first or third)",
    # "Direction_20"    -> "If the current element of the array <= 0 or not int or not first or third",
    # Direction_1000"   -> "If the current element of the array can not be taken in case of end of array"

    va_data.set('Direction...direction', 'The_code_of_the_direction_is _unknown')

      
    #va_data['i_main']['v'] += 1 # pointed on the next element of array
    local_data.set('Index of current element of array...i_main', local_data.get('Index of current element of array...i_main') + 1)
    #if va_data['i_main']['v'] > len(va_data['M']['v']) - 1:
    if local_data.get('Index of current element of array...i_main') > len(local_data.get('Input array...M')) - 1:
      #va_data['va']['v']['direction']['d'] = "The end of array"
      #va_data['va']['v']['direction']['v'] = "Direction_1000"
      va_data.set('Direction...direction', 'Direction_1000')

      return

    # get current element of array      
    #va_data['current_element']['v'] = va_data['M']['v'][va_data['i_main']['v']]
    temp_array = local_data.get('Input array...M')
    local_data.set('The current element of array...current element', temp_array[local_data.get('Index of current element of array...i_main')])
    #if va_data['current_element']['v'] > 0: 
    if local_data.set('The current element of array...current element') > 0:
      #va_data['va']['v']['direction']['d'] = "The current element is a positive number"
      #va_data['va']['v']['direction']['v'] = "Direction_10"
      va_data.set('Direction...direction', 'Direction_10')

      return

    #if not (va_data['current_element']['v'] > 0):
    if not local_data.set('The current element of array...current element') > 0:      
      #va_data['va']['v']['direction']['d'] = "The current element is not a positive number"
      #va_data['va']['v']['direction']['v'] = "Direction_20"
      va_data.set('Direction...direction', 'Direction_20')

      return