import pandas as pd

data = pd.read_csv('data.txt', sep=' ', names=['Date', 'Time', 'IA', 'CommunicateModuleIA',
                                               'Rssi', 'ProtectState', 'AlarmState',
                                               'BmsState', 'EqualizeState', 'Power', 'Capacity',
                                               'DischargeCurrentAverage', 'DischargeCurrentMax',
                                               'DischargeCurrent', 'ChargeCurrent', 'VoltageTotal',
                                               'VoltageSingleMax', 'VoltageSigleMin', 'TemperatureAverage',
                                               'TemperatureMax', 'TemperatureMin', 'TemperatureMos'])
# 行数
row = data.shape[0]
# 列数
column = data.shape[1]

# 遍历
for i in range(row):
    data.loc[i][1] = str(data.loc[i][1]).split('.')[0]
    for j in range(3, column):
        data.loc[i][j] = str(data.loc[i][j]).split(':')[1]

# 生成表格
data.to_csv('data.csv')
