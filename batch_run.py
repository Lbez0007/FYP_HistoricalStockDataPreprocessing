import glob
import os
import time
import papermill as pm
import ntpath


ROOT_DIR = os.path.abspath(os.curdir)

path_trends = ROOT_DIR + '\\trends'
csvfiles = glob.glob(path_trends + "/*.csv")

# for j, file in enumerate(csvfiles):
#     filename = ntpath.basename(file)
#     trd_variant = filename.split("GoogleTrendsAdjusted",1)[1]
#     trd_variant = trd_variant[:-4] # up until ".csv"
#     pm.execute_notebook('preprocessData10d_3rdP_GoogleTrd.ipynb', 'out.ipynb', parameters={ "trend_file_name": filename, "trends_variant": trd_variant})

for i, file in enumerate(csvfiles):
    filename = ntpath.basename(file)
    trd_variant = filename.split("GoogleTrendsAdjusted",1)[1]
    trd_variant = trd_variant[:-4]
    pm.execute_notebook('preprocessDataLSTM_Trends_3dprice_GoogleTrd.ipynb', 'out.ipynb', parameters={"trend_days": 7, "trend_file_name": filename, "trends_variant": trd_variant})