def getDirection(va_data, local_data):

    # In this function below we are determine the direction depending on the current element of the array.

    # "Direction_10"    -> "If the current element of the array > 0 and int and (first or third)",
    # "Direction_20"    -> "If the current element of the array <= 0 or not int or not first or third",
    # Direction_1000"   -> "If the current element of the array can not be taken in case of end of array"

    va_data.set('Direction...direction', 'The_code_of_the_direction_is _unknown')

    local_data.set('Index of current element of array...i_main', local_data.get('Index of current element of array...i_main') + 1)
    
    if local_data.get('Index of current element of array...i_main') > len(local_data.get('Input array...M')) - 1:
      va_data.set('Direction...direction', 'Direction_1000')

      return

    temp_array = local_data.get('Input array...M')
    local_data.set('The current element of array...current element', temp_array[local_data.get('Index of current element of array...i_main')])
  
    if local_data.get('The current element of array...current element') > 0:

      va_data.set('Direction...direction', 'Direction_10')

      return

    if not local_data.get('The current element of array...current element') > 0:      

      va_data.set('Direction...direction', 'Direction_20')

      return
