
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df1 = pd.read_pickle("./models/Anexo_A.pkl")
df = pd.DataFrame(df1)

newdataH= df1.iloc[:45,:]


xd = newdataH.reset_index() #sacar index

#Eliminar Columnas que no me interesan
xd = xd.drop(['level_0'], axis=1) #Eliminar tabla

#Renombrar Filas
xd = xd.rename({'level_1':'Diputado'}, axis='columns')

#Totales por filas SI, NO, ABSTENCION

D1 = xd[0].value_counts()
D2 = xd[1].value_counts()
D3 = xd[2].value_counts()
D4 = xd[3].value_counts()
D5 = xd[4].value_counts()
D6 = xd[5].value_counts()
D7 = xd[6].value_counts()
D8 = xd[7].value_counts()
D9 = xd[8].value_counts()
D10 = xd[9].value_counts()
D11 = xd[10].value_counts()
D12 = xd[11].value_counts()
D13 = xd[12].value_counts()
D14 = xd[13].value_counts()
D15 = xd[14].value_counts()
D16 = xd[15].value_counts()
D17 = xd[16].value_counts()
D18 = xd[17].value_counts()
D19 = xd[18].value_counts()
D20 = xd[19].value_counts()
D21 = xd[20].value_counts()
D22 = xd[21].value_counts()
D23 = xd[22].value_counts()
D24 = xd[23].value_counts()
D25 = xd[24].value_counts()
D26 = xd[25].value_counts()
D27 = xd[26].value_counts()
D28 = xd[27].value_counts()
D29 = xd[28].value_counts()
D30 = xd[29].value_counts()
D31 = xd[30].value_counts()
D32 = xd[31].value_counts()
D33 = xd[32].value_counts()
D34 = xd[33].value_counts()
D35 = xd[34].value_counts()
D36 = xd[35].value_counts()
D37 = xd[36].value_counts()
D38 = xd[37].value_counts()
D39 = xd[38].value_counts()
D40 = xd[39].value_counts()
D41 = xd[40].value_counts()
D42 = xd[41].value_counts()
D43 = xd[42].value_counts()
D44 = xd[43].value_counts()
D45 = xd[44].value_counts()

test = pd.DataFrame([D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20,D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,D32,D33,D34,D35,D36,D37,D38,D39,D40,D41,D42,D43,D44,D45])

D1V = xd['Diputado'].iloc[0]
D2V = xd['Diputado'].iloc[1]
D3V = xd['Diputado'].iloc[4]
D4V = xd['Diputado'].iloc[4]
D5V = xd['Diputado'].iloc[4]
D6V = xd['Diputado'].iloc[5]
D7V = xd['Diputado'].iloc[6]
D8V = xd['Diputado'].iloc[7]
D9V = xd['Diputado'].iloc[8]
D10V = xd['Diputado'].iloc[9]
D11V = xd['Diputado'].iloc[10]
D12V = xd['Diputado'].iloc[11]
D13V = xd['Diputado'].iloc[12]
D14V = xd['Diputado'].iloc[13]
D15V = xd['Diputado'].iloc[14]
D16V = xd['Diputado'].iloc[15]
D17V = xd['Diputado'].iloc[16]
D18V = xd['Diputado'].iloc[17]
D19V = xd['Diputado'].iloc[18]
D20V = xd['Diputado'].iloc[19]
D21V = xd['Diputado'].iloc[20]
D22V = xd['Diputado'].iloc[21]
D23V = xd['Diputado'].iloc[22]
D24V = xd['Diputado'].iloc[23]
D25V = xd['Diputado'].iloc[24]
D26V = xd['Diputado'].iloc[25]
D27V = xd['Diputado'].iloc[26]
D28V = xd['Diputado'].iloc[27]
D29V = xd['Diputado'].iloc[28]
D30V = xd['Diputado'].iloc[29]
D31V = xd['Diputado'].iloc[30]
D32V = xd['Diputado'].iloc[31]
D33V = xd['Diputado'].iloc[32]
D34V = xd['Diputado'].iloc[33]
D35V = xd['Diputado'].iloc[34]
D36V = xd['Diputado'].iloc[35]
D37V = xd['Diputado'].iloc[36]
D38V = xd['Diputado'].iloc[37]
D39V = xd['Diputado'].iloc[38]
D40V = xd['Diputado'].iloc[39]
D41V = xd['Diputado'].iloc[40]
D42V = xd['Diputado'].iloc[41]
D43V = xd['Diputado'].iloc[42]
D44V = xd['Diputado'].iloc[43]
D45V = xd['Diputado'].iloc[44]

test.insert(0,"Diputado",[D1V,D2V,D3V,D4V,D5V,D6V,D7V,D8V,D9V,D10V,D11V,D12V,D13V,D14V,D15V,D16V,D17V,D18V,D19V,D20V,D21V,D22V,D23V,D24V,D25V,D26V,D27V,D28V,D29V,D30V,D31V,D32V,D33V,D34V,D35V,D36V,D37V,D38V,D39V,D40V,D41V,D42V,D43V,D44V,D45V],True)

test.fillna(0, inplace = True)

print(test)
