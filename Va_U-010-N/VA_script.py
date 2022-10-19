def getVaScript():
    va_script = {
      "Action_000":{
          "_agent_position":{
              "en-US":"In Init block of VA-box",
              "ru-RU":"В блоке Init VA-box"
          },
          "_action_description":{
              "_010":"--> init action"
          },
          "Direction_10":"Action_010",  "_010":" > 0)",
          "Direction_20":"Action_020",  "_010":" <= 0",
          "Direction_1000":"Action_9000",  "_010":"The end of array"
      },
      "Action_010":{
          "_agent_position":{
              "en-US":"The v-agent is adding current element of array to the sum_01",
              "ru-RU":"v-agent добавляет текущий элемент массива к sum_01"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_10":"Action_010",  "_010":" > 0)",
          "Direction_20":"Action_020",  "_010":" <= 0",
          "Direction_1000":"Action_9000",  "_010":"The end of array"
      },
      "Action_020":{
          "_agent_position":{
              "en-US":"The v-agent is skipping the current element of array",
              "ru-RU":"v-agent пропускает текущий элемент массива"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_10":"Action_010",  "_010":" > 0)",
          "Direction_20":"Action_020",  "_010":" <= 0",
          "Direction_1000":"Action_9000",  "_010":"The end of array"
      },   
      "Action_9000":{
          "_agent_position":{
              "en-US":"The v-agent found the end of array",
              "ru-RU":"v-agent нашел конец массива"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_10":"Action_END",  "_010":" > 0 and int and (first or third)",
          "Direction_20":"Action_END",  "_010":" <= 0 or not int or not first or third",
          "Direction_1000":"Action_END",  "_010":"The end of array"
      }
    }

    return va_script
    