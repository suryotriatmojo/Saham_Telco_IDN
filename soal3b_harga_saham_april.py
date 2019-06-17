import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style = 'darkgrid')

xl = pd.read_csv('dataSaham/EXCL.JK.csv', parse_dates = ['Date'])
xl_apr = xl[(xl['Date'] > '2019-03-29') & (xl['Date'] < '2019-05-01')]

smart = pd.read_csv('dataSaham/FREN.JK.csv', parse_dates = ['Date'])
smart_apr = smart[(smart['Date'] > '2019-03-29') & (smart['Date'] < '2019-05-01')]

indosat = pd.read_csv('dataSaham/ISAT.JK.csv', parse_dates = ['Date'])
indosat_apr = indosat[(indosat['Date'] > '2019-03-29') & (indosat['Date'] < '2019-05-01')]

telkom = pd.read_csv('dataSaham/TLKM.JK.csv', parse_dates = ['Date'])
telkom_apr = telkom[(xl['Date'] > '2019-03-29') & (telkom['Date'] < '2019-05-01')]

plt.figure('Harga Historis Saham Provider Telco Indonesia (April 2019)', figsize = (12,8))
plt.plot(xl_apr['Date'], xl_apr['Close'], color = 'green', label = 'PT XL Axiata Tbk')
plt.plot(smart_apr['Date'], smart_apr['Close'], color = 'cyan', label = 'PT Smartfren Telecom Tbk')
plt.plot(indosat_apr['Date'], indosat_apr['Close'], color = 'blue', label = 'PT Indosat Tbk')
plt.plot(telkom_apr['Date'], telkom_apr['Close'], color = 'red', label = 'PT Telekomunikasi Indonesia Tbk')

plt.suptitle('Harga Historis Saham Provider Telco Indonesia (April 2019)')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation = 45)

label = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(label, loc = 'upper center', bbox_to_anchor = (0.5, 1.05), ncol = 4, frameon = False)

plt.show()