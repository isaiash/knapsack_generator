import os
import random

coef_name = [16, 31]
n_name = [50,100,200,400,800]
count = 0
for i, coef_max in enumerate([2**16, 2**31]):
	for j, n_max in enumerate([50000, 100000, 200000, 400000, 800000]):
		for type_ in [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16]:
			for k in range(100):
				n_elements = random.randint(2, n_max)
				coefficient_size = random.randint(2, coef_max)
				call = 'cd dataset_'+str(coef_name[i])+'_'+str(n_name[j])+'k ; ../generator '+str(n_elements)+' '+str(coefficient_size)+' '+str(type_)+' '+str(k)+' 1000 '+str(count)
				print(call)
				os.system(call)
				count += 1
