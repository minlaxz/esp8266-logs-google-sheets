from datetime import datetime, time
now_time = datetime.now().time()

def get_data_list():
    new_data = list()
    new_data.append(str(datetime.now()))
    # A Done DATE
    new_data.append(28.5)
    # B Done TEMP
    new_data.append(65.8)
    # C Done HUMIDITY
    new_data.append(0) if now_time >= time(18,00) or now_time <= time(6,00) else new_data.append(1)
    # D Done Day Time
    new_data.append(0)
    # E Done Raining
    new_data.append('Second One.')
    # F Done Message

    return new_data

# def get_data_dic():
#     new_data = dict()
#     new_data['Date'] = datetime.now()
#     new_data['TEMP'] = 28.5
#     new_data['HUMI'] = 65.9
#     new_data['DAY'] =
#     return new_data