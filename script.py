"""
Code to convert all .dat files (ECG signals) in a folder to CSV format 
@author: Abhishek Patil
"""
import wfdb #WaveForm-Database package. A library of tools for reading, writing, and processing WFDB signals and annotations.
import pandas as pd
import numpy as np
import glob


dat_files=glob.glob('*.dat') #Get list of all .dat files in the current folder
df=pd.DataFrame(data=dat_files)
df.to_csv("files_list.csv",index=False,header=None) #Write the list to a CSV file
files=pd.read_csv("files_list.csv",header=None)

for i in range(1,len(files)+1):
	recordname=str(files.iloc[[i]])
	print(recordname[:-4])
	recordname_new=recordname[-7:-4] #Extracting just the filename part (will differ from database to database)
	record = wfdb.rdsamp(recordname_new)
	record=np.asarray(record[0])
	path=recordname_new+".csv"
	np.savetxt(path,record,delimiter=",") #Writing the CSV for each record
	print("Files done: %s/%s"% (i,len(files)))

print("\nAll files done!")	

