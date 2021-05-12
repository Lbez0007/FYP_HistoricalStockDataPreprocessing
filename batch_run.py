import papermill as pm

pm.execute_notebook('preprocessDataLSTM_Trends_3dprice.ipynb','out.ipynb', parameters = {"trend_days":3})
pm.execute_notebook('preprocessDataLSTM_Trends_3dprice.ipynb','out.ipynb', parameters = {"trend_days":5})
pm.execute_notebook('preprocessDataLSTM_Trends_3dprice.ipynb','out.ipynb', parameters = {"trend_days":7})
pm.execute_notebook('preprocessDataLSTM_Trends_3dprice.ipynb','out.ipynb', parameters = {"trend_days":9})
pm.execute_notebook('preprocessDataLSTM_Trends_3dprice_normalized.ipynb','out.ipynb', parameters = {"trend_days":3})
pm.execute_notebook('preprocessDataLSTM_3dprice.ipynb','out.ipynb')