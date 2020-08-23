import os
import numpy as np
path = '/Users/aastha/Desktop/For Bromide_09.10.2019'
from natsort import natsorted
files = natsorted(os.listdir(path))
my_array = np.array(files)
my_array1 = [None]*len(my_array);
my_array2 = [None]*len(my_array);
for i in range(0,len(my_array)):
    my_array1[i] = my_array[i];
    
for i in range(0,len(my_array)):
    my_array2[i] = my_array[i];
    
for i in range(0,len(my_array1)):
    my_array1[i] = my_array1[i][8:-9]

for i in range(0,len(my_array2)):
    my_array2[i] = my_array2[i][-5:-4]

with open('/Users/aastha/Desktop/Nova Bromine R (1).txt') as f:
      lines1 = f.read().splitlines()
      
with open('/Users/aastha/Desktop/Nova Bromine G (1).txt') as f:
     lines2 = f.read().splitlines()
     
with open('/Users/aastha/Desktop/Nova Bromine B (1).txt') as f:
      lines3 = f.read().splitlines()
      
with open('/Users/aastha/Desktop/Vans Bromine R (1).txt') as f:
      lines4 = f.read().splitlines()
      
with open('/Users/aastha/Desktop/Vans Bromine G (1).txt') as f:
     lines5 = f.read().splitlines()
     
with open('/Users/aastha/Desktop/Vans Bromine B (1).txt') as f:
      lines6 = f.read().splitlines()
            
with open('/Users/aastha/Desktop/Baldwin Bromine R (1).txt') as f:
      lines7 = f.read().splitlines()
      
with open('/Users/aastha/Desktop/Baldwin Bromine G (1).txt') as f:
     lines8 = f.read().splitlines()
     
with open('/Users/aastha/Desktop/Baldwin Bromine B (1).txt') as f:
      lines9 = f.read().splitlines()            

import pandas as pd
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
df = pd.DataFrame({'number' : my_array2, 'ppm': my_array1, 'NovaR': lines1, 'NovaG': lines2, 'NovaB': lines3, 'VansR': lines4, 'VansG': lines5, 'VansB': lines6, 'BaldwinR': lines7, 'BaldwinG': lines8, 'BaldwinB': lines9})
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
df.to_excel(r'/Users/aastha/Desktop/demo.xlsx', index = False)
