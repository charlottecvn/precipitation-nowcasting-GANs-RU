# Variables to set for the specific user
USER_FOLDER = '/home/ccambiervannoote'
project_FOLDER = 'precipitation-nowcasting-GANs-RU'

# When not rendering a new list with IDs, use the default option as listed below
basic_IDs_npy = 'list_IDs201520_avg001mm.npy'

# Global variables that point to the correct directory
path_data = '/ceph/knmimo/thesis_charlotte/'

path_code = f'{USER_FOLDER}/{project_FOLDER}/'

path_project = '//'

dir_basic_IDs = path_code + f'/data/{basic_IDs_npy}'

dir_train_IDs = path_code + f'/data/train_randomsplit.npy'
dir_val_IDs = path_code + f'/data/val_randomsplit.npy'
dir_test_IDs = path_code + f'/data/test_randomsplit.npy'

dir_rtcor = path_data + 'dataset_rtcor/'

dir_prep = 'preprocessed/'
dir_rtcor_prep = path_data + dir_prep + 'rtcor_prep/'

dir_labels = path_data + dir_prep + 'rtcor_rain_labels/'
dir_labels_heavy = path_data + dir_prep + 'rtcor_heavy_rain_labels/'

prefix_rtcor = 'RAD_NL25_RAC_5M_'
