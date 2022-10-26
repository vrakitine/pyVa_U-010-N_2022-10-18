from VaScript import getVaScript


def setup(va_data):

    ### Start | The VAOP variables setting


    if 'va' not in va_data:
        va_data['va']= {}
        va_data['va']['v'] = {}
        va_data['va']['d'] = "The VAOP sysrem variables"   

    va_data['va']['v']['jump'] = {}
    va_data['va']['v']['jump']['v'] = 0
    va_data['va']['v']['jump']['d'] = "The sequential number of the v-agent's jump"

    va_data['va']['v']['max_jump'] = {}
    va_data['va']['v']['max_jump']['v'] = 1000
    va_data['va']['v']['max_jump']['d'] = "The max number of the v-agent's jump. It is for prevent looping."

    va_data['va']['v']['locale_lang_code_defaulf'] = {}
    va_data['va']['v']['locale_lang_code_defaulf']['v'] = 'en-US'
    va_data['va']['v']['locale_lang_code_defaulf']['d'] = "The default locale language code"

    if  isNotDefinedOutsideOfVaBox(va_data['va']['v'],'locale_lang_code'):
        va_data['va']['v']['locale_lang_code'] = {}
        va_data['va']['v']['locale_lang_code']['v'] = 'en-US'
        va_data['va']['v']['locale_lang_code']['d'] = "The locale language code"

    va_data['va']['v']['agent_position'] = {}
    va_data['va']['v']['agent_position']['v'] = 'Unknown'
    va_data['va']['v']['agent_position']['d'] = "It is info about what is v-agent doing at this moment"

    va_data['va']['v']['script'] = {}
    va_data['va']['v']['script']['v'] = getVaScript()
    va_data['va']['v']['script']['d'] = "VA script"

    va_data['va']['v']['previous_action'] = {}
    va_data['va']['v']['previous_action']['v'] = 'Unknown'
    va_data['va']['v']['previous_action']['d'] = "The previous Action"

    va_data['va']['v']['current_action'] = {}
    va_data['va']['v']['current_action']['v'] = 'Action_000'
    va_data['va']['v']['current_action']['d'] = "The current Action"

    va_data['va']['v']['direction'] = {}
    va_data['va']['v']['direction']['v'] = "Direction_10"
    va_data['va']['v']['direction']['d'] = "Direction"

    ### for va-traking
    if isNotDefinedOutsideOfVaBox(va_data['va']['v'],'is_tracking_on'):
        va_data['va']['v']['is_tracking_on'] = {}
        va_data['va']['v']['is_tracking_on']['v'] = False
        va_data['va']['v']['is_tracking_on']['d'] = "Is tracking ON? (True/False)"

    if isNotDefinedOutsideOfVaBox(va_data['va']['v'],'content_of_va_tracking_row'):
        va_data['va']['v']['content_of_va_tracking_row'] = {}
        va_data['va']['v']['content_of_va_tracking_row']['v'] = ['jump', 'previous_action', 'direction', 'agent_position']
        va_data['va']['v']['content_of_va_tracking_row']['d'] = "The content of va-tracking row"

    if isNotDefinedOutsideOfVaBox(va_data['va']['v'],'tracking_actions'):
        va_data['va']['v']['tracking_actions'] = {}
        va_data['va']['v']['tracking_actions']['v'] = getVaScript().keys()
        va_data['va']['v']['tracking_actions']['d'] = "The list of actions to track"

    if isNotDefinedOutsideOfVaBox(va_data['va']['v'],'jump_pause_after_actions'):
        va_data['va']['v']['jump_pause_after_actions'] = {}
        va_data['va']['v']['jump_pause_after_actions']['v'] = []
        va_data['va']['v']['jump_pause_after_actions']['d'] = "The jump pause after actions"

    va_data['va']['v']['direction_action_tracking'] = {}
    va_data['va']['v']['direction_action_tracking']['v'] = []
    va_data['va']['v']['direction_action_tracking']['d'] = "The direction action tracking"

    ### End | The VAOP variables setting
    
    return va_data

def isNotDefinedOutsideOfVaBox(var_array, var_key_name):
    temp = True
    if var_key_name in var_array:
        if ('v' in var_array[var_key_name]) and ('d' in var_array[var_key_name]):
            temp = False

    return temp