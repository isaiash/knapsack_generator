import os
import numpy as np
from glob import glob
from scipy.stats.stats import pearsonr

LEVELS = [
	'dataset_16_50k',
	'dataset_16_100k',
	'dataset_16_200k',
	'dataset_16_400k',
	'dataset_16_800k',
	'dataset_31_50k',
	'dataset_31_100k',
	'dataset_31_200k',
	'dataset_31_400k',
	'dataset_31_800k'
]

def get_features(id_, num_elem, cap, weights, values):
    mean_w = np.mean(weights)
    median_w = np.median(weights) 
    desv_w = np.std(weights)
    min_w = min(weights)
    max_w = max(weights)
    mean_v = np.mean(values)
    median_v = np.median(values) 
    desv_v = np.std(values)
    min_v = min(values)
    max_v = max(values) 
    p_coef, p_value = pearsonr(weights, values)

    if (mean_w == 0 or median_w == 0 or desv_w == 0 or mean_v == 0 or median_v == 0 or desv_v ==0):
        print('ALARMAA')
        return -1
    
    return [id_,
    		num_elem, # n
            cap, # cap
            cap/mean_w,
            cap/median_w,
            cap/desv_w,
            mean_w/mean_v,
            median_w/median_v,
            desv_w/desv_v,
            max_w - min_w,
            max_v - min_v,
            mean_w, 
            median_w, 
            desv_w, 
            min_w, 
            max_w, 
            mean_v, 
            median_v, 
            desv_v, 
            min_v, 
            max_v,
            p_coef]

f= open('features/feats',"w+")
for i, level in enumerate(LEVELS):
	print(level)
	range_ = range(1500*i, 1500*(i+1))
	files_ = glob(level+'/*')
	for file_ in range_:
		path = level+'/'+str(file_)
		if path not in files_ or os.path.getsize(path) == 0:
			print('alerta',file)
		else:
			read_file = open(path, "r")
			for line in read_file:
				items = line.split(' ')
				id_ = int(items[0])
				n_ = int(items[1])
				cap_ = int(items[2])
				weights_ = list(map(int, items[3:n_+3]))
				values_ = list(map(int, items[n_+3:-1]))
			f.write(' '.join(str(x) for x in get_features(id_,n_,cap_,weights_, values_))+'\n')
f.close() 
