'''
Created on 2019. 8. 6.

@author: tlsdn
'''
import pandas as pd
import numpy as np

accident_data = pd.read_csv("./accident.csv", sep='|', encoding='CP949' )
print(accident_data.shape)
accident_data.head(10)
colum_list = accident_data.columns[0].split(',')
print('colum_list',colum_list)
print('accident_data',accident_data)
accident_data_num = accident_data.to_numpy()
print('accident_data_num',accident_data_num)
print('accident_data_num_list',)
print('accident_data_num_list_string',accident_data_num[0][0])
print('accident_data_num_list_string_makeList',accident_data_num[0][0].split(','))
print('accident_data_num_list_string_makeList_takeAttribute',accident_data_num[0][0].split(',')[0])
make_list = []
count = 0
for i in accident_data_num:
    print('데이터{0}'.format(i))
    accident_data_num_list_string_makeList = i[0].split(',')

    list_len = len(accident_data_num_list_string_makeList)
    print('accident_data_num_list_string_makeList 의 길이:',list_len)
    if count ==0:
        for num in range(list_len):
            make_list.append([])
    print(make_list)
    count_k=0
    for j in accident_data_num_list_string_makeList:
        print(j)
        print(make_list[count_k].append(j))
        count_k+=1
    print('make_list',make_list)
    count += 1
result = dict(zip(colum_list,make_list))
print('result',result)
result_pd = pd.DataFrame(result,columns=colum_list)
print(result_pd['법규위반'])
print('result_pd :',result_pd)
print(result_pd['발생건수'])



