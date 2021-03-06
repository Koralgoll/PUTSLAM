from subprocess import call
import subprocess
import sys
import glob
import os
from math import ceil

call("rm test", shell=True); 
call("touch test", shell=True); 

call("rm resultSummary", shell=True); 
call("touch resultSummary", shell=True); 

prevDatasetName = "";

print("NAME   VORpeTra   VORpeRot   VOAte   g2oRpeTra   g2oRpeRot   g2oAte\n");
call("echo \"NAME   VORpeTra   VORpeRot   VOAte   g2oRpeTra   g2oRpeRot   g2oAte\" >> resultSummary" , shell=True); 
for root, dirs, files in os.walk("../../results/"):
	rpeTra = "";
	rpeRot = "";
	ateTra = "";
	time = "";
	
	for file in files:
		#print(file)
		if 'g2oRpe.res' in file or 'VORpe.res' in file:
			call("echo \"" + root + "\" >> test" , shell=True); 
			call("cat " + root +"/" + file + " | grep translational_error.rmse |  sed 's/translational_error.rmse/RPE.rmse/'>> test" , shell=True); 	
			call("cat " + root +"/" + file + " | grep rotational_error.rmse |  sed 's/rotational_error.rmse/RPE.rmse/'>> test" , shell=True);


			p1 = subprocess.Popen("cat " + root +"/" + file, stdout=subprocess.PIPE, shell=True);
			p2 = subprocess.Popen("grep translational_error.rmse", stdin=p1.stdout, stdout=subprocess.PIPE, shell=True);
			p3 = subprocess.Popen("sed 's/translational_error.rmse //'", stdin=p2.stdout, stdout=subprocess.PIPE, shell=True);
			p4 = subprocess.Popen("sed 's/ m//'", stdin=p3.stdout, stdout=subprocess.PIPE, shell=True);	
			p5 = subprocess.Popen("head -c -1", stdin=p4.stdout, stdout=subprocess.PIPE, shell=True);		
			rpeTra, err = p5.communicate();

			if 'g2oRpe.res' in file:
				g2oRpeTra = str(round( float(rpeTra.rstrip()), 3));
			elif 'VORpe.res' in file:
				VORpeTra = str(round( float(rpeTra.rstrip()), 3));

			
		     	p1 = subprocess.Popen("cat " + root +"/" + file, stdout=subprocess.PIPE, shell=True);
			p2 = subprocess.Popen("grep rotational_error.rmse", stdin=p1.stdout, stdout=subprocess.PIPE, shell=True);
			p3 = subprocess.Popen("sed 's/rotational_error.rmse //'", stdin=p2.stdout, stdout=subprocess.PIPE, shell=True);	
			p4 = subprocess.Popen("sed 's/ deg//'", stdin=p3.stdout, stdout=subprocess.PIPE, shell=True);	
			p5 = subprocess.Popen("head -c -1", stdin=p4.stdout, stdout=subprocess.PIPE, shell=True);	
			rpeRot, err = p5.communicate();

			if 'g2oRpe.res' in file:
				g2oRpeRot = str(round( float(rpeRot.rstrip()), 3));
			elif 'VORpe.res' in file:
				VORpeRot = str(round( float(rpeRot.rstrip()), 3));

		if 'g2oAte.res' in file or 'VOAte.res' in file:
			 
			tmp = root.split("/");	
			prevDatasetName = tmp[2];		
			if "BACKUP" in tmp[3]:
				continue;
			
		     	call("cat " + root +"/" + file + " | grep absolute_translational_error.rmse |  sed 's/absolute_translational_error.rmse/ATE.rmse/' >> test" , shell=True); 

		     	p1 = subprocess.Popen("cat " + root +"/" + file, stdout=subprocess.PIPE, shell=True);
			p2 = subprocess.Popen("grep absolute_translational_error.rmse", stdin=p1.stdout, stdout=subprocess.PIPE, shell=True);
			p3 = subprocess.Popen("sed 's/absolute_translational_error.rmse //'", stdin=p2.stdout, stdout=subprocess.PIPE, shell=True);	
			p4 = subprocess.Popen("sed 's/ m//'", stdin=p3.stdout, stdout=subprocess.PIPE, shell=True);	
			p5 = subprocess.Popen("head -c -1", stdin=p4.stdout, stdout=subprocess.PIPE, shell=True);	
			ateTra, err = p5.communicate();

			if 'VOAte.res' in file:
				VOAte = str(round( float(ateTra), 3))
			elif 'g2oAte.res' in file:
				g2oAte = str(round( float(ateTra), 3))
				tmp = root.split("/");
				print(tmp[3] + "\t" + VORpeTra + "  " + VORpeRot + "  " + VOAte + "  " + g2oRpeTra + "  " + g2oRpeRot + "  " + g2oAte +"\n");
				call("echo \"" + tmp[3] + " & " + VORpeTra + " & " + VORpeRot + " & " + VOAte + " & " + g2oRpeTra + " & " + g2oRpeRot + " & " + g2oAte + " \" >> resultSummary" , shell=True); 
			
call("rm test", shell=True); 
call("mv resultSummary ../../results/", shell=True); 
