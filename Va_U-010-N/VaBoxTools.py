


def getAgentPosition(va_data):
    va_data['va']['v']['agent_position']['v'] = "Now in [" + va_data['va']['v']['previous_action']['v'] + "]"
    if '_agent_position' in va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]:
        if va_data['va']['v']['locale_lang_code']['v'] in va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position']:
            va_data['va']['v']['agent_position']['v'] = va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position'][va_data['va']['v']['locale_lang_code']['v']]
        if va_data['va']['v']['agent_position']['v'] == '':
            if va_data['va']['v']['locale_lang_code_defaulf']['v'] in va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position']:
                va_data['va']['v']['agent_position']['v'] = va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position'][va_data['va']['v']['locale_lang_code_defaulf']['v']]
        if va_data['va']['v']['locale_lang_code']['v'] not in va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position']:
            if va_data['va']['v']['locale_lang_code_defaulf']['v'] in va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position']:
                va_data['va']['v']['locale_lang_code']['v'] = va_data['va']['v']['script']['v'][va_data['va']['v']['previous_action']['v']]['_agent_position'][va_data['va']['v']['locale_lang_code_defaulf']['v']]
    
    return va_data 

def VA_tracking_row(va_data):
    va_data = getAgentPosition(va_data)
    print("va-agent tracking -->")
    for temp in va_data['va']['v']['content_of_va_tracking_row']['v']:
        print("\t" + temp ,"= [" + str(va_data['va']['v'][temp]['v']) + "] <-- " +  va_data['va']['v'][temp]['d'])
      
    return va_data 

def VA_set_direction_action_tracking(va_data):
    temp = str(va_data['current_element']['v']) + ' - ' + va_data['va']['v']['direction']['v']  + ' - ' + va_data['va']['v']['current_action']['v']
    va_data['va']['v']['direction_action_tracking']['v'].append(temp)
    print
    return va_data

def VA_print_direction_action_tracking(va_data):
    for temp in va_data['va']['v']['direction_action_tracking']['v']:
        print(temp)

    return va_data