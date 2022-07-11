 # -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:05:15 2021

@author: Jiho3
"""
import random

#%% 8.23 1-MWCNT+大型蚤
#Biological Uptake and Depuration of Carbon Nanotubes by Daphnia magna
body_burden = pd.DataFrame()
for i in (0.04,0.1,0.4):
    new_data = processed_data.loc[(processed_data['element']=='MWCNTs')&(processed_data['Organism']=='Daphnia magna')&(processed_data['pH']==7.5)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    temp_processed_data['Exposure concentration(mg/L)'] = i
    number = 20
    sel_data = pd.DataFrame(columns = new_data.columns)
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,48,number)
    sel_data['Exposure time(h)']
    sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)  #这里改模型
    body_burden[i] = 10**bcf * i
body_burden.index = sel_data['Exposure time(h)']
plt.plot(body_burden.index,body_burden)
# plt.text(60,0,'小尺寸')
plt.legend(body_burden.columns)

# # 测试数据
# sel_data = processed_data.loc[(processed_data['element']=='MWCNTs')&(processed_data['Organism']=='Daphnia magna')&(processed_data['pH']==7.5)
#                        &(processed_data['Exposure concentration(mg/L)']==0.04)]
# variable = 0.3
# sel_data['Exposure concentration(mg/L)'] = variable
# temp_processed_data = sel_data.iloc[1]# 复制的次数
# number = 20
# for t in range(number-sel_data.shape[0]):
#     sel_data.loc[sel_data.shape[0]] = temp_processed_data
# sel_data['Exposure time(h)'] = np.linspace(0,48,number)
# sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
# sel_data['Organism'] = le.transform(sel_data['Organism'])
# sel_data['element'] = le2.transform(sel_data['element'])
# sel_data['shape'] = le3.transform(sel_data['shape'])
# x = sel_data.drop(['LOG10(BCF)'],axis=1)
# bcf = rf.predict(x)  #这里改模型
# test_burden = 10**bcf * variable
# plt.plot(sel_data['Exposure time(h)'],test_burden)


#%% 9.7. 3-石墨烯+大型蚤
# Bioaccumulation of 14C‑Labeled Graphene in an Aquatic Food Chain through Direct Uptake or Trophic Transfer
body_burden = pd.DataFrame()
for i in (0.025,0.05,0.1,0.25):
    new_data = processed_data.loc[(processed_data['element']=='Graphene')&(processed_data['Organism']=='Daphnia magna')&(processed_data['pH']==7.8)
                       &(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    temp_processed_data['Exposure concentration(mg/L)'] = i
    number = 20
    sel_data = pd.DataFrame(columns = new_data.columns)
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,48,number)
    sel_data['Exposure time(h)']
    sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)  #这里改模型
    body_burden[i] = 10**bcf * i
body_burden.index = sel_data['Exposure time(h)']
plt.plot(body_burden.index,body_burden)
# plt.text(60,0,'小尺寸')
plt.legend(body_burden.columns)
#%% 9.7. 4-C60+大型蚤  12.11更新
body_burden = pd.DataFrame()
for i in (2.5,1,0.1):
    new_data = processed_data.loc[(processed_data['element']=='C60')&(processed_data['Organism']=='Daphnia magna')]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)']=i
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,48,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)
#%% 9.7. 
# 废弃5-ZnO+罗非鱼
body_burden = pd.DataFrame()
for i in (1,10):
    sel_data = processed_data.loc[(processed_data['element']=='ZnO')&(processed_data['Organism']=='Oreochromis niloticus')&
                      (processed_data['Size']==20)
                       &(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = sel_data.iloc[1]# 复制的次数
    for t in range(50-sel_data.shape[0]):
            sel_data.loc[t] = temp_processed_data
    sel_data.columns
    sel_data
    sel_data['Exposure time(h)'] = np.linspace(0,338,50)
    sel_data['Exposure time(h)']
    time = sel_data['Exposure time(h)']
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    x = sel_data.drop(['element','LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * i
body_burden.index = sel_data['Exposure time(h)']/24
plt.plot(sel_data['Exposure time(h)'],body_burden)
plt.text(300,0,sel_data['Size'][0])
plt.legend(body_burden.columns)
#%% 
#  9.16. 6-TiO2+crayfish废弃
body_burden = pd.DataFrame()
for i in (25,125,250):
    sel_data = processed_data.loc[(processed_data['element']=='TiO2')&(processed_data['Organism']=='Crayfish')&(processed_data['pH']==7.6)
                       &(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = sel_data.iloc[1]# 复制的次数
    number = 50
    for t in range(number-sel_data.shape[0]):
             sel_data.loc[t] = temp_processed_data
    sel_data.columns
    sel_data
    sel_data['Exposure time(h)'] = np.linspace(0,672,number)
    sel_data['Exposure time(h)']
    time = sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])  #需要将字符串格式转为label
    x = sel_data.drop(['element','LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * i
body_burden.index = sel_data['Exposure time(h)']/24
plt.plot(sel_data['Exposure time(h)']/24,body_burden)
plt.legend(body_burden.columns)

#%% 9.17. 7-SeNP+Oreochromis niloticus
body_burden = pd.DataFrame()
for i in (1.23,1.81,2.79):
    sel_data = processed_data.loc[(processed_data['element']=='SeNPs')&(processed_data['Organism']=='Oreochromis niloticus')
                       &(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = sel_data.iloc[1]# 复制的次数
    number = 50
    for t in range(number-sel_data.shape[0]):
             sel_data.loc[t] = temp_processed_data
    sel_data.columns
    sel_data
    sel_data['Exposure time(h)'] = np.linspace(0,2160,number)
    sel_data['Exposure time(h)']
    time = sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    x = sel_data.drop(['element','LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * i
body_burden.index = sel_data['Exposure time(h)']/24
plt.plot(sel_data['Exposure time(h)']/24,body_burden)
plt.legend(body_burden.columns)
#%% 12.10 8.9-不同表面修饰的MWCNT-大型蚤
body_burden = pd.DataFrame()
new_data = processed_data.loc[(processed_data['element']=='MWCNTs')&(processed_data['Organism']=='Daphnia magna')
                              &(processed_data['Exposure concentration(mg/L)']==0.056)]  #更改浓度获得不同数据
temp_processed_data = new_data.iloc[1]# 复制的次数
sel_data = pd.DataFrame(columns = new_data.columns)
number = 20
for t in range(number):
    sel_data = sel_data.append(temp_processed_data)
sel_data['Exposure time(h)'] = np.linspace(0,48,number)
sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
sel_data['shape'] = le3.transform(sel_data['shape'])
sel_data['NOM'] = le4.transform(sel_data['NOM'])
x = sel_data.drop(['LOG10(BCF)','element','Organism'],axis=1)
bcf = rf.predict(x)
body_burden = 10**bcf * 0.056                                                     #浓度要改
# body_burden.index = sel_data['Exposure time(h)']
plt.plot(sel_data['Exposure time(h)'],body_burden)
plt.legend(body_burden)

#%% 计算kin和kout的r2
from sklearn.metrics import r2_score
filename = 'D:/我的坚果云/# Part 2/12.13-RF-TK.xlsx'
k_data = pd.read_excel(filename,header=0)
data_tk = k_data['TK-train'].dropna()
data_rf = k_data['RF-train'].dropna()
print(r2_score(data_tk,data_rf))
k_data.columns  #看特征名

#%% 9.18 8.9-不同粒径的ZnO-卤虫
body_burden = pd.DataFrame()
for i in (10,50,100):
    sel_data = processed_data.loc[(processed_data['element']=='ZnO')&(processed_data['Organism']=='Artemia salina')&
                                  (processed_data['Size']==200)&(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = sel_data.iloc[1]# 复制的次数
    number = 50
    for t in range(number-sel_data.shape[0]):
             sel_data.loc[t] = temp_processed_data
    sel_data.columns
    sel_data
    sel_data['Exposure time(h)'] = np.linspace(0,100,number)
    sel_data['Exposure time(h)']
    time = sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * i
body_burden.index = sel_data['Exposure time(h)']
plt.plot(sel_data['Exposure time(h)'],body_burden)
plt.legend(body_burden.columns)

#%%
# 10.11  不同纳米材料+大型蚤
body_burden = pd.DataFrame()
nano = magna.element.unique()

for i in nano:  
    new_data = processed_data.loc[(processed_data['element']=='Graphene')&(processed_data['Organism']=='Daphnia magna')
                       &(processed_data['Exposure concentration(mg/L)']==0.1)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]
#调整特征值
    temp_processed_data['element'] = i
    # temp_processed_data['Size'] = 
#调整特征值
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['substance'] = sel_data['element'].apply(lambda x: 1 if x in substance else 0)
    sel_data['compound'] = sel_data['element'].apply(lambda x: 1 if x in compound else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0)
        #更改molar mass值
    element_molar = {'AgNPs':107.86,'CuO':79.55,'ZnO':81.38,'ZnNPs':65.38,'TiO2':79.9,'C60':12,
      'CuNPs':63.54,'Graphene':12,'MWCNTs':12,'CeO2':172,'AuNPs':196.96}
    for e in element_molar.keys():
        if e == sel_data['element'].unique():
            sel_data['molar mass'] = element_molar[e]
    #更改molar mass 值
    sel_data.columns
    sel_data
    sel_data['Exposure time(h)'] = np.linspace(0,48,number)
    sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * 0.1
body_burden.index = sel_data['Exposure time(h)']
plt.plot(sel_data['Exposure time(h)'],body_burden)
plt.legend(body_burden.columns)


#%%
# 10.18  不同尺寸石墨烯+大型蚤
body_burden = pd.DataFrame()
nano = magna.element.unique()

for i in range(20,110,20):
    new_data = processed_data.loc[(processed_data['element']=='Graphene')&(processed_data['Organism']=='Daphnia magna')
                       &(processed_data['Exposure concentration(mg/L)']==0.1)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]
    #调整特征值
    temp_processed_data['Size'] = i  
    # temp_processed_data['Size'] = 
    #调整特征值
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    #更改molar mass 值
    sel_data['Exposure time(h)'] = np.linspace(0,48,number)
    sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * 0.1
body_burden.index = sel_data['Exposure time(h)']
plt.plot(sel_data['Exposure time(h)'],body_burden)
plt.text(40,50,'石墨烯')
plt.legend(body_burden.columns)

#%%
# 10.18  不同尺寸C60+大型蚤
body_burden = pd.DataFrame()
nano = magna.element.unique()

for i in range(20,110,20):
    new_data = processed_data.loc[(processed_data['element']=='Graphene')&(processed_data['Organism']=='Daphnia magna')
                       &(processed_data['Exposure concentration(mg/L)']==0.1)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]
    #调整特征值
    temp_processed_data['Size'] = i  
    temp_processed_data['element'] = 'C60' 
    temp_processed_data['shape'] = 'spherical' 
    #调整特征值
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['substance'] = sel_data['element'].apply(lambda x: 1 if x in substance else 0)
    sel_data['compound'] = sel_data['element'].apply(lambda x: 1 if x in compound else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0)
    #更改molar mass值
    element_molar = {'AgNPs':107.86,'CuO':79.55,'ZnO':81.38,'ZnNPs':65.38,'TiO2':79.9,'C60':12,
      'CuNPs':63.54,'Graphene':12,'MWCNTs':12,'CeO2':172,'AuNPs':196.96}
    for e in element_molar.keys():
        if e == sel_data['element'].unique():
            sel_data['molar mass'] = element_molar[e]
    #更改molar mass 值
    sel_data['Exposure time(h)'] = np.linspace(0,48,number)
    sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * 0.1
body_burden.index = sel_data['Exposure time(h)']
plt.plot(sel_data['Exposure time(h)'],body_burden)
plt.text(40,50,'C60')
plt.legend(body_burden.columns)



#%%
# 10.18  不同尺寸TiO2+大型蚤
body_burden = pd.DataFrame()
nano = magna.element.unique()

for i in range(20,110,20):
    new_data = processed_data.loc[(processed_data['element']=='Graphene')&(processed_data['Organism']=='Daphnia magna')
                       &(processed_data['Exposure concentration(mg/L)']==0.1)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]
    #调整特征值
    temp_processed_data['Size'] = i  
    temp_processed_data['element'] = 'TiO2' 
    #调整特征值
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['substance'] = sel_data['element'].apply(lambda x: 1 if x in substance else 0)
    sel_data['compound'] = sel_data['element'].apply(lambda x: 1 if x in compound else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0)
    #更改molar mass值
    element_molar = {'AgNPs':107.86,'CuO':79.55,'ZnO':81.38,'ZnNPs':65.38,'TiO2':79.9,'C60':12,
      'CuNPs':63.54,'Graphene':12,'MWCNTs':12,'CeO2':172,'AuNPs':196.96}
    for e in element_molar.keys():
        if e == sel_data['element'].unique():
            sel_data['molar mass'] = element_molar[e]
    #更改molar mass 值
    sel_data['Exposure time(h)'] = np.linspace(0,48,number)
    sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * 0.1
body_burden.index = sel_data['Exposure time(h)']
plt.plot(sel_data['Exposure time(h)'],body_burden)
plt.text(40,50,'TiO2' )
plt.legend(body_burden.columns)




#%%
# 10.19  不同尺寸ZnO+大型蚤 30.50.90
body_burden = pd.DataFrame()
nano = magna.element.unique()

for i in [30,50,90]:
    new_data = processed_data.loc[(processed_data['element']=='ZnO')&(processed_data['Organism']=='Daphnia magna')]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]
    #调整特征值
    temp_processed_data['Size'] = i 
    # temp_processed_data['element'] = 'TiO2' 
    temp_processed_data['Exposure concentration(mg/L)'] = 1
    #调整特征值
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    
    sel_data['substance'] = sel_data['element'].apply(lambda x: 1 if x in substance else 0)
    sel_data['compound'] = sel_data['element'].apply(lambda x: 1 if x in compound else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0)
    #更改molar mass值
    element_molar = {'AgNPs':107.86,'CuO':79.55,'ZnO':81.38,'ZnNPs':65.38,'TiO2':79.9,'C60':12,
      'CuNPs':63.54,'Graphene':12,'MWCNTs':12,'CeO2':172,'AuNPs':196.96}
    for e in element_molar.keys():
        if e == sel_data['element'].unique():
            sel_data['molar mass'] = element_molar[e]
    #更改molar mass 值
    sel_data['Exposure time(h)'] = np.linspace(0,24,number)
    sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * 1
body_burden.index = sel_data['Exposure time(h)']
plt.plot(sel_data['Exposure time(h)'],body_burden)
plt.text(40,50,'ZnO' )
plt.legend(body_burden.columns)

#%% 10.19 1-MWCNT+大型蚤    12.29更新
#剔除后再拟合 无法完成，因为2篇文献的数据差距很大
body_burden = pd.DataFrame()
for i in (0.04,0.1,0.4):
    new_data = processed_data.loc[(processed_data['element']=='MWCNTs')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Size']==70)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #调整特征值
    temp_processed_data['Exposure concentration(mg/L)'] = i
    #调整特征值
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,48,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x_std = std.transform(x)                                                                    #数据标准化
    bcf = xgb.predict(x_std)  #这里改模型
    body_burden[i] = 10**bcf
# plt.plot(sel_data['Exposure time(h)'],body_burden)

for i in body_burden.columns:
    plt.scatter(sel_data['Exposure time(h)'],body_burden[i])
plt.legend(body_burden.columns)
# # 测试数据
# sel_data = processed_data.loc[(processed_data['element']=='MWCNTs')&(processed_data['Organism']=='Daphnia magna')&(processed_data['pH']==7.5)
#                        &(processed_data['Exposure concentration(mg/L)']==0.04)]
# variable = 0.3
# sel_data['Exposure concentration(mg/L)'] = variable
# temp_processed_data = sel_data.iloc[1]# 复制的次数
# number = 20
# for t in range(number-sel_data.shape[0]):
#     sel_data.loc[sel_data.shape[0]] = temp_processed_data
# sel_data['Exposure time(h)'] = np.linspace(0,48,number)
# sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
# sel_data['Organism'] = le.transform(sel_data['Organism'])
# sel_data['element'] = le2.transform(sel_data['element'])
# sel_data['shape'] = le3.transform(sel_data['shape'])
# x = sel_data.drop(['LOG10(BCF)'],axis=1)
# bcf = rf.predict(x)  #这里改模型
# test_burden = 10**bcf * variable
# plt.plot(sel_data['Exposure time(h)'],test_burden)


#%% 10.20 2-石墨烯+斑马鱼
#小尺寸的
body_burden = pd.DataFrame()
for i in (0.05,0.075,0.25):
    sel_data = processed_data.loc[(processed_data['element']=='Graphene')&(processed_data['Organism']=='Danio rerio')&(processed_data['temperature']==27)&(processed_data['Size']==31.5)
                       &(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = sel_data.iloc[1]# 复制的次数
    for t in range(50-sel_data.shape[0]):
            sel_data.loc[sel_data.shape[0]] = temp_processed_data
    sel_data.columns
    sel_data
    sel_data['Exposure time(h)'] = np.linspace(0,72,50)
    sel_data['Exposure time(h)']
    sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * i

plt.plot(sel_data['Exposure time(h)'],body_burden)
plt.text(60,0,'小尺寸')
plt.legend(body_burden.columns)

#%% 10.20 2-L-石墨烯+斑马鱼   12.10更改
#大尺寸的
body_burden = pd.DataFrame()
for i in (0.05,0.075,0.25):
    new_data = processed_data.loc[(processed_data['element']=='Graphene')&(processed_data['Organism']=='Danio rerio')
                                  &(processed_data['Size']==770)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,72,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)


#%% 10.21 2-S-石墨烯+斑马鱼   12.10更改
#小尺寸的
body_burden = pd.DataFrame()
for i in (0.05,0.075,0.25):
    new_data = processed_data.loc[(processed_data['element']=='Graphene')&(processed_data['Organism']=='Danio rerio')
                                  &(processed_data['Size']==31.5)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,72,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)


#%% 10.22 不同nomAgNPs+斑马鱼
#小尺寸的
body_burden = pd.DataFrame()
for i in ('None','HA','FA'):
    new_data = processed_data.loc[(processed_data['element']=='AgNPs')&(processed_data['Organism']=='Danio rerio')
                                  &(processed_data['Surface modification']=='PVP-')&(processed_data['NOM']==i)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    # temp_processed_data['Hydrodynamic diameter'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,168,number)
    sel_data['Exposure time(h)']
    sel_data['Exposure time(h)']
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * 0.02
body_burden.index = sel_data['Exposure time(h)']/24
plt.plot(sel_data['Exposure time(h)'],body_burden)
# plt.text(60,0,'小尺寸')
plt.legend(body_burden.columns)
#因为没有其他HA和FA的数据，所以暂时做不了
# 测试

#%%
# 10.25  1mg/L和10mg/L的ZnO暴露卤虫
#Acute toxicity, uptake, and elimination of zinc oxide nanoparticles (ZnONPs) using saltwater microcrustacean, Artemia franciscana
body_burden = pd.DataFrame()
for i in (1,10):
    new_data = processed_data.loc[(processed_data['element']=='ZnO')&(processed_data['Organism']=='Artemia salina')
                                  &(processed_data['Size']==32.28)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,24,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)','element','Organism'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * i
body_burden.index = sel_data['Exposure time(h)']
plt.plot(sel_data['Exposure time(h)'],body_burden)
# plt.text(60,0,'小尺寸')
plt.legend(body_burden.columns)

# 结果：10mg/L的bb相比真实值太低了，因为本篇文献报道的bb值太高了

#%%
# 10.25 20nm和200nm的ZnO暴露卤虫  12.11更新
# Comparative evaluation of impact of Zn and ZnO nanoparticles on brine shrimp (Artemia salina) larvae: effects of particle size and solubility on toxicity
body_burden = pd.DataFrame()
for i in (10,50,100): 
    new_data = processed_data.loc[(processed_data['element']=='ZnO')&(processed_data['Organism']=='Artemia salina')
                                  &(processed_data['Size']==20)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,96,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)



#%%
# 10.25 21.33nm的ZnO暴露卤虫   12.11更新
# Effects of Zn and ZnO Nanoparticles on Artemia salina and Daphnia magna Organisms: Toxicity, Accumulation and Elimination 
body_burden = pd.DataFrame()
for i in (0.2,1,5,10,25,50): 
    new_data = processed_data.loc[(processed_data['element']=='ZnO')&(processed_data['Organism']=='Artemia salina')
                                  &(processed_data['Size']==21.33)&(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,72,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)



#%%
# 10.26 52.54\89.5nm的ZnNPs暴露卤虫
# Effects of Zn and ZnO Nanoparticles on Artemia salina and Daphnia magna Organisms: Toxicity, Accumulation and Elimination 
body_burden = pd.DataFrame()
for i in (50,25,10,5,1,0.2): 
    new_data = processed_data.loc[(processed_data['element']=='ZnNPs')&(processed_data['Organism']=='Artemia salina')
                                  &(processed_data['Size']==89.5)&(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,72,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * i
body_burden.index = sel_data['Exposure time(h)']
plt.plot(sel_data['Exposure time(h)'],body_burden)
# plt.text(60,0,'小尺寸')
plt.legend(body_burden.columns)

#%%
# 10.26 52.54\89.5nm的ZnNPs暴露大型蚤
# Effects of Zn and ZnO Nanoparticles on Artemia salina and Daphnia magna Organisms: Toxicity, Accumulation and Elimination 
body_burden = pd.DataFrame()
for i in (50,25,10,5,1,0.2): 
    new_data = processed_data.loc[(processed_data['element']=='ZnNPs')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Size']==89.5)&(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,72,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)

#%%
# 10.26 21.33nm的ZnO暴露大型蚤  12.13更新
# Effects of Zn and ZnO Nanoparticles on Artemia salina and Daphnia magna Organisms: Toxicity, Accumulation and Elimination 
body_burden = pd.DataFrame()
for i in (50,25,10): 
    new_data = processed_data.loc[(processed_data['element']=='ZnO')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Size']==21.33)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)']=i
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,72,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']/24
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)



#%%
# 10.27 TiO2暴露大型蚤
# Toxicity and bioaccumulation of TiO2 nanoparticle aggregates in Daphnia magna
body_burden = pd.DataFrame()
for i in (0.1,1): 
    new_data = processed_data.loc[(processed_data['element']=='TiO2')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Size']==21)&(processed_data['Exposure concentration(mg/L)']==0.1)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,24,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)






#%%
# 10.27 TiO2暴露大型蚤-不同表面修饰
# Aging Influences on the Biokinetics of Functional TiO2 Nanoparticles with Different Surface Chemistries in Daphnia magna
body_burden = pd.DataFrame()
for i in (1,10): 
    new_data = processed_data.loc[(processed_data['element']=='TiO2')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Surface modification']=='SiO2')
                                  &(processed_data['Size']==30)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,72,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)

#%%
# 10.27 CuNPs暴露丰年虾-
#Comparative effects of Cu (60–80 nm) and CuO (40 nm) nanoparticles in Artemia salina: Accumulation, elimination and oxidative stress
body_burden = pd.DataFrame()
for i in (0.2,1,5,10,25,50): 
    new_data = processed_data.loc[(processed_data['element']=='CuNPs')&(processed_data['Organism']=='Artemia salina')]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,72,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)

#%%
# 12.10 AgNPs-大型蚤
#Bioaccumulation of silver in Daphnia magna:Waterborne and dietary exposure to nanoparticles and dissolved silver body_burden = pd.DataFrame()
body_burden = pd.DataFrame()
for i in (0.005,0.01): 
    new_data = processed_data.loc[(processed_data['element']=='AgNPs')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,48,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)
#%%
# 12.30 CuO-大型蚤
#Bioaccumulation of silver in Daphnia magna:Waterborne and dietary exposure to nanoparticles and dissolved silver body_burden = pd.DataFrame()
body_burden = pd.DataFrame()
for i in (0.07,0.15): 
    new_data = processed_data.loc[(processed_data['element']=='CuO')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Exposure concentration(mg/L)']==i)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,336,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['logBB','element','Organism'],axis=1)
    x = std.transform(x)
    bcf = xgb.predict(x)
    body_burden[i] = 10**bcf
body_burden.index = sel_data['Exposure time(h)']/24
# plt.plot(body_burden.index,body_burden)
# plt.text(60,0,'小尺寸')
for i in body_burden.columns:
    plt.scatter(body_burden.index,body_burden[i])
plt.legend(body_burden.columns)

#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响
logbcf = pd.DataFrame()
for i in (20,40,60,100): 
    new_data = processed_data.loc[(processed_data['element']=='CuNPs')&(processed_data['Organism']=='Artemia salina')
                                  &(processed_data['Exposure time(h)']==48)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = i
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(0,10,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
plt.plot(logbcf.index,logbcf)
# plt.text(60,0,'小尺寸')
plt.legend(logbcf.columns)



#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响
logbcf = pd.DataFrame()
for i in (20,40,60,100): 
    new_data = processed_data.loc[(processed_data['element']=='TiO2')&(processed_data['Organism']=='Daphnia magna')&(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = i
    # temp_processed_data['Exposure time(h)'] = 24   
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(0.2,9.8,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)


#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:尺寸-MWCNTs
# =============================================================================
# ['element', 'molar mass', 'Surface modification', 'Size',
#        'Hydrodynamic diameter', 'Zeta potential', 'Organism', 'DO', 'pH',
#        'temperature', 'shape', 'bodylength(mm)', 'NOM', 'Exposure time(h)',
#        'Exposure concentration(mg/L)', 'LOG10(BCF)', 'substance', 'compound',
#        'C']
# =============================================================================
logbcf = pd.DataFrame()
for i in (20,50,100): 
    new_data = processed_data.loc[(processed_data['element']=='MWCNTs')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = i
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(0.3,10,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)

#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:hd-MWCNTs
logbcf = pd.DataFrame()
for i in range(0,1500,200): 
    new_data = processed_data.loc[(processed_data['element']=='MWCNTs')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Hydrodynamic diameter'] = i
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 50
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(0,10,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)
    
    
#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:尺寸-ZnO
logbcf = pd.DataFrame()
for i in (20,40,60,90): 
    new_data = processed_data.loc[(processed_data['element']=='ZnO')&(processed_data['Organism']=='Daphnia magna')&(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = i
    # temp_processed_data['Exposure time(h)'] = 24   
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(0,9,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)

#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:ZnO-hd
logbcf = pd.DataFrame()
for i in range(0,1500,200): 
    new_data = processed_data.loc[(processed_data['element']=='ZnO')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Hydrodynamic diameter'] = i
    # temp_processed_data['Exposure time(h)'] = 24   
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 10
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(0,10,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)

#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:size-Graphene
logbcf = pd.DataFrame()
for i in (20,50,100,500): 
    new_data = processed_data.loc[(processed_data['element']=='Graphene')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = i
    # temp_processed_data['Exposure time(h)'] = 24   
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(1,10,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)


#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:size-C60
logbcf = pd.DataFrame()
for i in (20,50,100): 
    new_data = processed_data.loc[(processed_data['element']=='C60')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = i
    # temp_processed_data['Exposure time(h)'] = 24   
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(0.5,10,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)


#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:size-CuNPs
logbcf = pd.DataFrame()
for i in (20,50,100): 
    new_data = processed_data.loc[(processed_data['element']=='CuNPs')&(processed_data['Organism']=='Daphnia magna')]
                                  # &(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = i
    temp_processed_data['Exposure time(h)'] = 24   
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(0,9.5,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    # sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    x.drop(['element','Organism'],axis=1,inplace=True) 
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)


#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:size-AuNPs
logbcf = pd.DataFrame()
for i in (20,50,100): 
    new_data = processed_data.loc[(processed_data['element']=='AuNPs')]
                                  # &(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = i
    temp_processed_data['Exposure time(h)'] = 24   
    temp_processed_data['Organism'] = 'Daphnia magna'
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(1,10,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)

#%%  11.10
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:size-ZnNPs
logbcf = pd.DataFrame()
for i in (20,40,60,100): 
    new_data = processed_data.loc[(processed_data['element']=='ZnNPs')&(processed_data['Organism']=='Daphnia magna')]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = i
    temp_processed_data['Exposure time(h)'] = 24   
    # temp_processed_data['Organism'] = 'Daphnia magna'
    # temp_processed_data['Size'] = 31.5
    # temp_processed_data['Hydrodynamic diameter'] = 1000   
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.linspace(1,9,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = sel_data['Exposure concentration(mg/L)']
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)



#%%  11.16  采取随机取特征的方式
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:尺寸-MWCNTs
# =============================================================================
# ['element', 'molar mass', 'Surface modification', 'Size',
#        'Hydrodynamic diameter', 'Zeta potential', 'Organism', 'DO', 'pH',
#        'temperature', 'shape', 'bodylength(mm)', 'NOM', 'Exposure time(h)',
#        'Exposure concentration(mg/L)', 'LOG10(BCF)', 'substance', 'compound',
#        'C']
# =============================================================================
logbcf = pd.DataFrame()
for i in range(5): 
    new_data = processed_data.loc[(processed_data['element']=='MWCNTs')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = random.randint(10,100)
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    temp_processed_data['Exposure time(h)'] = random.randint(0,48)
    temp_processed_data['Hydrodynamic diameter'] = random.randint(10,1000)
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.append(np.linspace(0,1,int(number*2/3)),np.linspace(1,5,int(number*1/3)))
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    # sel_data['Organism'] = le.transform(sel_data['Organism'])
    # sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = np.log10(sel_data['Exposure concentration(mg/L)'])
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)


#%%  11.16  采取随机取特征的方式
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:尺寸-MWCNTs
# =============================================================================
# ['element', 'molar mass', 'Surface modification', 'Size',
#        'Hydrodynamic diameter', 'Zeta potential', 'Organism', 'DO', 'pH',
#        'temperature', 'shape', 'bodylength(mm)', 'NOM', 'Exposure time(h)',
#        'Exposure concentration(mg/L)', 'LOG10(BCF)', 'substance', 'compound',
#        'C']
# =============================================================================
logbcf = pd.DataFrame()
for i in range(5): 
    new_data = processed_data.loc[(processed_data['element']=='C60')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = random.randint(10,100)
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    temp_processed_data['Exposure time(h)'] = random.randint(0,48)
    temp_processed_data['Hydrodynamic diameter'] = random.randint(10,1000)
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.append(np.linspace(0,1,int(number*2/3)),np.linspace(1,5,int(number*1/3)))
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = np.log10(sel_data['Exposure concentration(mg/L)'])
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)

#%%  11.16  采取随机取特征的方式
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:尺寸-MWCNTs
# =============================================================================
# ['element', 'molar mass', 'Surface modification', 'Size',
#        'Hydrodynamic diameter', 'Zeta potential', 'Organism', 'DO', 'pH',
#        'temperature', 'shape', 'bodylength(mm)', 'NOM', 'Exposure time(h)',
#        'Exposure concentration(mg/L)', 'LOG10(BCF)', 'substance', 'compound',
#        'C']
# =============================================================================
logbcf = pd.DataFrame()
for i in range(5): 
    new_data = processed_data.loc[(processed_data['element']=='Graphene')&(processed_data['Organism']=='Daphnia magna')
                                  &(processed_data['Exposure time(h)']==24)]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = random.randint(10,100)
    # temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['Size'] = 31.5
    temp_processed_data['Exposure time(h)'] = random.randint(0,48)
    temp_processed_data['Hydrodynamic diameter'] = random.randint(10,1000)
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.append(np.linspace(0,1,int(number*2/3)),np.linspace(1,5,int(number*1/3)))
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = np.log10(sel_data['Exposure concentration(mg/L)'])
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)

#%%  11.16  采取随机取特征的方式
# 考虑做一些图，表征尺寸、浓度等因素对BCF的影响:尺寸-MWCNTs
# =============================================================================
# ['element', 'molar mass', 'Surface modification', 'Size',
#        'Hydrodynamic diameter', 'Zeta potential', 'Organism', 'DO', 'pH',
#        'temperature', 'shape', 'bodylength(mm)', 'NOM', 'Exposure time(h)',
#        'Exposure concentration(mg/L)', 'LOG10(BCF)', 'substance', 'compound',
#        'C']
# =============================================================================
logbcf = pd.DataFrame()
for i in range(5): 
    new_data = processed_data.loc[(processed_data['element']=='CeO2')]
                                  # &(processed_data['Organism']=='Daphnia magna')]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Size'] = random.randint(10,100)
    temp_processed_data['Organism'] = 'Daphnia magna'
    # temp_processed_data['Size'] = 31.5
    temp_processed_data['Exposure time(h)'] = random.randint(0,48)
    temp_processed_data['Hydrodynamic diameter'] = random.randint(10,1000)
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 30
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure concentration(mg/L)'] = np.append(np.linspace(0,1,int(number*2/3)),np.linspace(1,5,int(number*1/3)))
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    logbcf[i] = bcf
logbcf.index = np.log10(sel_data['Exposure concentration(mg/L)']) #给浓度取对数
# plt.scatter(logbcf.index,logbcf[20])
for p in logbcf.columns:
    plt.scatter(logbcf.index,logbcf[p])
    # plt.text(60,0,'小尺寸')
    plt.legend(logbcf.columns)


#%%  11.18  采取随机取特征的方式
# 考虑做一些图，横坐标是生物的种类

# =============================================================================
# ['element', 'molar mass', 'Surface modification', 'Size',
#        'Hydrodynamic diameter', 'Zeta potential', 'Organism', 'DO', 'pH',
#        'temperature', 'shape', 'bodylength(mm)', 'NOM', 'Exposure time(h)',
#        'Exposure concentration(mg/L)', 'LOG10(BCF)', 'substance', 'compound',
#        'C']
# =============================================================================

b =  ['Daphnia magna','Capitella teleta','Artemia salina','Cyprinus carpio Larvae','Scrobicularia plana',
      'Limnodrilus hoffmeisteri','Danio rerio','Mytilus galloprovincialis','Nereis diversicolor']
nanoparticles = ['ZnO', 'Graphene', 'AgNPs', 'ZnNPs', 'C60', 'TiO2', 'CeO2', 'CuO',
       'MWCNTs', 'CuNPs', 'AuNPs']
length = {'Daphnia magna':1,'Capitella teleta':1,'Artemia salina':1.75,'Cyprinus carpio Larvae':5.3,'Scrobicularia plana':5,'Limnodrilus hoffmeisteri':30,'Danio rerio':35,
          'Mytilus galloprovincialis':40,'Nereis diversicolor':100}
logbcf = pd.DataFrame()
for t in nanoparticles:
    new_data = processed_data.loc[(processed_data['element']==t)]  # 先选定纳米材料的种类，就不用变种类三列特征
    temp_processed_data = new_data.iloc[1]
    sel_data = pd.DataFrame(columns = new_data.columns)
    for i in range(3):
        temp_processed_data['Size'] = random.randint(10,100)
        temp_processed_data['Organism'] = 'Nereis diversicolor'  #在这里改生物名称
        for e in length.keys():
            if e == temp_processed_data['Organism']:
                temp_processed_data['bodylength(mm)'] = length[e]  #根据生物种类改变体长
        temp_processed_data['Exposure time(h)'] = random.randint(0,48)
        temp_processed_data['Hydrodynamic diameter'] = random.randint(10,1000)
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    # sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    x.drop(['element','Organism'],axis=1,inplace=True) 
    bcf = rf.predict(x)
    logbcf[t] = bcf



#%% 实验验证
# 11.26 Graphene暴露丰年虾-  与zyl数据比较
#查数据：250ug/L是1200ug/g， 100ug/L是300ug/g, 50ug/L是150ug/g
body_burden = pd.DataFrame()
for i in (0.05,0.1,0.2): 
    new_data = processed_data.loc[(processed_data['Organism']=='Artemia salina')]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['bodylength(mm)'] = 1

    temp_processed_data['element'] = 'CuO'
    # temp_processed_data['Size'] = 50
    # temp_processed_data['Hydrodynamic diameter'] = 1000  
    # temp_processed_data['Zeta potential'] = -90   #纯水-26.2，海水-9.0
    # temp_processed_data['shape'] = 'slice'
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['substance'] = sel_data['element'].apply(lambda x: 1 if x in substance else 0)
    sel_data['compound'] = sel_data['element'].apply(lambda x: 1 if x in compound else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0)
    #更改molar mass值
    element_molar = {'AgNPs':107.86,'CuO':79.55,'ZnO':81.38,'ZnNPs':65.38,'TiO2':79.9,'C60':12,
      'CuNPs':63.54,'Graphene':12,'MWCNTs':12,'CeO2':172,'AuNPs':196.96}
    for e in element_molar.keys():
        if e == sel_data['element'].unique():
            sel_data['molar mass'] = element_molar[e]
    sel_data['Exposure time(h)'] = np.linspace(0,72,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * i
body_burden.index = sel_data['Exposure time(h)']
plt.plot(body_burden.index,body_burden)
# plt.text(60,0,'小尺寸')
plt.legend(body_burden.columns)



#%% 实验验证
# 11.26 Graphene暴露大型蚤-  与我自己做的数据比较
#查数据：250ug/L是1200ug/g， 100ug/L是300ug/g, 50ug/L是150ug/g
body_burden = pd.DataFrame()
for i in (0.1,0.2): 
    new_data = processed_data.loc[(processed_data['Organism']=='Daphnia magna')&(processed_data['element']=='Graphene')]  #更改浓度获得不同数据
    temp_processed_data = new_data.iloc[1]# 复制的次数
    #
    temp_processed_data['Exposure concentration(mg/L)'] = i
    # temp_processed_data['bodylength(mm)'] = 1

    # temp_processed_data['element'] = 'Graphene'
    # temp_processed_data['Size'] = 50
    # temp_processed_data['Hydrodynamic diameter'] = 1000  
    # temp_processed_data['Zeta potential'] = -90   #纯水-26.2，海水-9.0
    # temp_processed_data['shape'] = 'slice'
    #
    sel_data = pd.DataFrame(columns = new_data.columns)
    number = 20
    for t in range(number):
        sel_data = sel_data.append(temp_processed_data)
    sel_data['substance'] = sel_data['element'].apply(lambda x: 1 if x in substance else 0)
    sel_data['compound'] = sel_data['element'].apply(lambda x: 1 if x in compound else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0)
    #更改molar mass值
    element_molar = {'AgNPs':107.86,'CuO':79.55,'ZnO':81.38,'ZnNPs':65.38,'TiO2':79.9,'C60':12,
      'CuNPs':63.54,'Graphene':12,'MWCNTs':12,'CeO2':172,'AuNPs':196.96}
    for e in element_molar.keys():
        if e == sel_data['element'].unique():
            sel_data['molar mass'] = element_molar[e]
    sel_data['Exposure time(h)'] = np.linspace(0,24,number)
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    sel_data['Organism'] = le.transform(sel_data['Organism'])
    sel_data['element'] = le2.transform(sel_data['element'])
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    bcf = rf.predict(x)
    body_burden[i] = 10**bcf * i
body_burden.index = sel_data['Exposure time(h)']
plt.plot(body_burden.index,body_burden)
# plt.text(60,0,'小尺寸')
plt.legend(body_burden.columns)


#%%  12.9-需要做TOC图片，结合动力学
# 考虑做一些图，横坐标是暴露时间。

# =============================================================================
# ['element', 'molar mass', 'Surface modification', 'Size',
#        'Hydrodynamic diameter', 'Zeta potential', 'Organism', 'DO', 'pH',
#        'temperature', 'shape', 'bodylength(mm)', 'NOM', 'Exposure time(h)',
#        'Exposure concentration(mg/L)', 'LOG10(BCF)', 'substance', 'compound',
#        'C']
# =============================================================================

organism =  ['Daphnia magna','Capitella teleta','Artemia salina','Cyprinus carpio Larvae','Scrobicularia plana',
      'Limnodrilus hoffmeisteri','Danio rerio','Mytilus galloprovincialis','Nereis diversicolor']
nanoparticles = ['ZnO', 'Graphene', 'AgNPs', 'ZnNPs', 'C60', 'TiO2', 'CeO2', 'CuO',
       'MWCNTs', 'CuNPs', 'AuNPs']
length = {'Daphnia magna':0.5,'Capitella teleta':1,'Artemia salina':1,'Cyprinus carpio Larvae':5.3,'Scrobicularia plana':5,'Limnodrilus hoffmeisteri':30,'Danio rerio':34.2,
          'Mytilus galloprovincialis':30,'Nereis diversicolor':90}
weight = {'Daphnia magna':0.015,'Capitella teleta':0.0028,'Artemia salina':0.0033,'Cyprinus carpio Larvae':5,'Scrobicularia plana':2700,'Limnodrilus hoffmeisteri':0.25,'Danio rerio':270,
          'Mytilus galloprovincialis':12900,'Nereis diversicolor':130}
logbcf = pd.DataFrame()
new_data = processed_data.loc[(processed_data['element']=='CeO2')]               #在这里改变纳米材料
for t in organism:
    # new_data = processed_data.loc[(processed_data['Organism']==t)]                      # 先选定纳米材料的种类，就不用变种类三列特征
    temp_processed_data = new_data.iloc[1]
    sel_data = pd.DataFrame(columns = new_data.columns)
    for i in range(20):
        # temp_processed_data['Size'] = random.randint(10,100)                        #不能在这里改，每个时间点的size都不一样
        conc = 0.1                                                                      #浓度
        temp_processed_data['Exposure concentration(mg/L)'] = conc
        temp_processed_data['Organism'] = t                                       #在这里改生物
        for e in length.keys():
            if e == temp_processed_data['Organism']:
                temp_processed_data['bodylength(mm)'] = length[e]                       #根据生物种类改变体长
                temp_processed_data['body weight(mg)'] = weight[e]                      #根据生物种类改变体重  
        # temp_processed_data['Hydrodynamic diameter'] = random.randint(10,1000)
        sel_data = sel_data.append(temp_processed_data)
    sel_data['Exposure time(h)'] = np.linspace(0,48,20)                         #不随机，采用数据中原本的值
    #随机改变的变量
    sel_data['Hydrodynamic diameter'] = random.randint(10,1000)
    sel_data['Size'] = random.randint(10,100)
    ###
    sel_data['Surface modification'] = le1.transform(sel_data['Surface modification'])
    #
    sel_data['vertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in vertebrate else 0)
    sel_data['invertebrate'] = sel_data['Organism'].apply(lambda x: 1 if x in invertebrate else 0)
    sel_data['plankton'] = sel_data['Organism'].apply(lambda x: 1 if x in plankton else 0)
    sel_data['shell'] = sel_data['Organism'].apply(lambda x: 1 if x in shell else 0)
    sel_data['metal'] = sel_data['element'].apply(lambda x: 1 if x in metal else 0)
    sel_data['C'] = sel_data['element'].apply(lambda x: 1 if x in C else 0) 
    #
    sel_data['shape'] = le3.transform(sel_data['shape'])
    sel_data['NOM'] = le4.transform(sel_data['NOM'])
    x = sel_data.drop(['LOG10(BCF)'],axis=1)
    x.drop(['element','Organism'],axis=1,inplace=True) 
    bcf = rf.predict(x)
    body_burden = 10**bcf * conc                                                        #浓度
    logbcf[t] = body_burden
    logbcf.index = sel_data['Exposure time(h)']
    
#density没变















