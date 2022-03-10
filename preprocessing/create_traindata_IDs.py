import os

from batchcreator_GAN import get_list_IDs
from datetime import datetime
import numpy as np

start_dt = datetime(2015,1,1,0,0)
end_dt =  datetime(2021,1,1,0,0)
x_length = 6
y_length = 1
filter_no_rain = 'avg0.01mm'
filename = 'list_IDs201520_avg001mm.npy'
print(os.getcwd())

list_IDs = get_list_IDs(start_dt, end_dt, x_length, y_length, filter_no_rain=filter_no_rain)
print(list_IDs[-1])
print(len(list_IDs))

np.save(filename, list_IDs)