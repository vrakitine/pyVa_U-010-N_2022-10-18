def getDirection(va_data):

    # In this function below we are determine the direction depending on the current element of the array.

    # "Direction_10"    -> "If the current element of the array > 0 and int and (first or third)",
    # "Direction_20"    -> "If the current element of the array <= 0 or not int or not first or third",
    # Direction_1000"   -> "If the current element of the array can not be taken in case of end of array"

    va_data['va']['v']['direction']['d'] = "The description of the direction is unknown"
    va_data['va']['v']['direction']['v'] = "The_code_of_the_direction_is _unknown"

      
    va_data['i_main']['v'] += 1 # pointed on the next element of array
    if va_data['i_main']['v'] > len(va_data['M']['v']) - 1:
      va_data['va']['v']['direction']['d'] = "The end of array"
      va_data['va']['v']['direction']['v'] = "Direction_1000"

      return va_data  #-----------> Direction_1000 "If the current element of the array can not be taken in case of end of array"

    # get current element of array      
    va_data['current_element']['v'] = va_data['M']['v'][va_data['i_main']['v']]

    if va_data['current_element']['v'] > 0: 
      va_data['va']['v']['direction']['d'] = "The current element is a positive number"
      va_data['va']['v']['direction']['v'] = "Direction_10"

      return va_data  #-----------> Direction_10

    if not (va_data['current_element']['v'] > 0):
      va_data['va']['v']['direction']['d'] = "The current element is not a positive number"
      va_data['va']['v']['direction']['v'] = "Direction_20"
      
      return va_data  #-----------> Direction_20  

    return va_data  
