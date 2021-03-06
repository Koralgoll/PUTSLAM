#
#	author: Michal Nowicki
#
from subprocess import call
import subprocess
import sys
import glob
import os


for datasetId in range(2,10):
	for kinectNo in range(1,3):
		print("python evaluate_ate.py Kin1vsKin2/dataset" + str(datasetId) + "/Kin1_groundtruth_recomputed.txt Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"_recomputed.txt --verbose --scale 1 --save_associations Kin1vsKin2/dataset" + str(datasetId) + "/Kin"+ str(kinectNo) + "_associations.res --save_errors Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"AteErrors.txt --plot Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"Ate.png > Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"Ate.res");

		call("python evaluate_ate.py Kin1vsKin2/dataset" + str(datasetId) + "/Kin1_groundtruth_recomputed.txt Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"_recomputed.txt --verbose --scale 1 --save_associations Kin1vsKin2/dataset" + str(datasetId) + "/Kin"+ str(kinectNo) + "_associations.res --save_errors Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"AteErrors.txt --plot Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"Ate.png > Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"Ate.res", shell=True);

		print("python evaluate_rpe.py Kin1vsKin2/dataset" + str(datasetId) + "/Kin1_groundtruth_recomputed.txt Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"_recomputed.txt --verbose --delta_unit 'f' --fixed_delta --save_errors Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"RpeErrors.txt --plot Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"Rpe.png > Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"Rpe.res");

		call("python evaluate_rpe.py Kin1vsKin2/dataset" + str(datasetId) + "/Kin1_groundtruth_recomputed.txt Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"_recomputed.txt --verbose --delta_unit 'f' --fixed_delta --save_errors Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"RpeErrors.txt --plot Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"Rpe.png > Kin1vsKin2/dataset" + str(datasetId) + "/Kin" + str(kinectNo) +"Rpe.res", shell=True);


