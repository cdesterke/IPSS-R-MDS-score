#!usr/bin/python3


"""
IPSS-R MDS score 
date: avril 2017
author: Christophe Desterke
christophe.desterke@gmail.com
python version 3.4
"""

#imports
import os
import time


# obtaining time date
horloge= time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime())

# definition of the variable continuer for exit interaction
continuer = True

while continuer:

	print("	--------------- ")
	print("	IPSS-R MDS ")
	print("	--------------- ")
	
	print("		",horloge)
	print("\n")

# input variables
	print (" Please enter your identifier: " , end =" ")
	identifier = input ()
	try:
		name = str (identifier)
	except ValueError:
		print('	Please enter an integrer number!')
		continue

	print(" 	Your Name is: ",name)
	
# pass one line for results	
	print("\n")

# cytogenetic score definition
	print(" Definition of the cytogenetic score, make your choice")
	print(" choice 0: -Y or del(11q)")
	print(" choice 1: normal or del(5q) or del(12p) of del(20q) or double including del(5q)")
	print(" choice 2: del(7q) or +8 or +19 or i(17q) any other single or double")
	print(" choice 3: -7, inv(3)/t(3q)/del(3q), double including -7/del(7q), complex 3 ab.")
	print(" choice 4: complex > 3ab.")
	print (" Please enter your cytogenetic choice: " , end =" ")
	karyo = input ()
	try:
		karyo = int (karyo)
	except ValueError:
		print('	Please enter an integrer number!')
		continue
	print("	Your karyotype score is: ",karyo)
	if karyo == 0:
		print ("	Conclusion cytogenetic: Very good group with median survival of 5.4 years!","\n")
	elif karyo == 1:
		print ("	Conclusion cytogenetic: Good group with median survival of 4.8 years!","\n")
	elif karyo == 2:
		print ("	Conclusion cytogenetic: Intermediate group with median survival of 2.7 years!","\n")
	elif karyo == 3:
		print ("	Conclusion cytogenetic: Poor group with median survival of 1.5 years!","\n")
	elif karyo == 4:
		print ("	Conclusion cytogenetic: Very poor group with median survival of 0.7 years!","\n")		
	else:
		print ("	Your karyotype score answer is not correct!","\n")
		continuer = False 


# definition of blast proportion
	print (" Please enter the proportion of blasts in bone marrow: " , end =" ")
	blast = input ()
	try:
		blast = float (blast)
	except ValueError:
		print('	Please enter a number!')
		continue
	
	print("	The medullary blast proportion is: ",blast)
	if blast <= 2:
		blastscore = 0
		print ("	blast score: ",blastscore)
	elif blast > 2 and blast < 5:
		blastscore = 1
		print ("	blast score: ",blastscore)
	elif blast >= 5 and blast <= 10:
		blastscore = 2
		print ("	blast score: ",blastscore)
	else:
		blastscore = 3
		print ("	blast score: ",blastscore)



# definition of hemoglobin value
	print (" Please enter the hemoglobin value: " , end =" ")
	hb = input ()
	try:
		hb = float (hb)
	except ValueError:
		print('	Please enter a number!')
		continue
	
	print("	The hemoglobin value is: ",hb)
	
	if hb >= 10:
		hbscore = 0
		print ("	hemoglobin score: ",hbscore)
	elif hb >= 8 and hb < 10:
		hbscore = 1
		print ("	hemoglobin score: ",hbscore)
	else:
		hbscore = 1.5
		print ("	hemoglobin score: ",hbscore)

# definition of platelet value

	print (" Please enter the platelet count G/L: " , end =" ")
	plt = input ()
	try:
		plt = float (plt)
	except ValueError:
		print('	Please enter a number!')
		continue

	print("	The platelet count G/L is: ",plt)
	
	if plt >= 100:
		pltscore = 0
		print ("	platelet score: ",pltscore)
	elif plt >= 50 and plt < 100:
		pltscore = 0.5
		print ("	platelet score: ",pltscore)
	else:
		pltscore = 1
		print ("	platelet score: ",pltscore)

# definition of neutrophil count
	print (" Please enter the absolute neutrophil count G/L: " , end =" ")
	anc = input ()
	try:
		anc = float (anc)
	except ValueError:
		print('	Please enter a number!')
		continue

	print("	The absolute neutrophil count G/L is: ",anc)	

	if anc >= 0.8:
		ancscore = 0
		print ("	ANC score: ",ancscore)
		
	else:
		ancscore = 1
		print ("	ANC score: ",ancscore)

# calcul IPSS-R score

	IPSS = karyo + blastscore + hbscore + pltscore + ancscore
	print ("----------------------------------------------------")
	print ("Calcul of MDS IPSS-R pronostic score: ",IPSS)
	
	if IPSS <= 1.5:
		print("	IPSS-R group score : Very low risk category")
		print("	Median survival 8.8 years")
	elif IPSS > 1.5 and IPSS <= 3:
		print("	IPSS-R group score : Low risk category")
		print("	Median survival 5.3 years")
	elif IPSS > 3 and IPSS <= 4.5:
		print("	IPSS-R group score : Intermediate risk category")
		print("	Median survival 3.0 years")
	elif IPSS > 4.5 and IPSS <= 6:
		print("	IPSS-R group score : High risk category")
		print("	Median survival 1.8 years")
	else:
		print("	IPSS-R group score : Very High risk category")
		print("	Median survival 0.8 year")
	print ("----------------------------------------------------")
	print ("	reference: Greenberg PL: Blood 2012","\n")

# interaction with exit of the software	
	quitter =  input('Do you want to exit (y/n)? ')
	if quitter == "y" or quitter == "Y":
		continuer = False
os.system("pause")


