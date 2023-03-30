name = input("Enter name here: ")

#...initialize looping variable, assume 'yes' as the first answer
continueYN = "y"
 
while continueYN == "y" or "Y":
   #...get temperature input from the user
   sDegreeF = input("Enter next temperature in degrees Fahrenheit (F):")
 
   #...convert text entry to number value that can be used in equations
   nDegreeF = int(sDegreeF)

 
   name = name

   #...convert temperature from F to Celsius
   nDegreeC = (nDegreeF - 32) * 5 / 9
 
   print ("Temperature in degrees C is:", nDegreeC)
 
   #...check for temperature below freezing..
   if nDegreeF < 33:
      print ("Pack long underwear,", name)
 
   #...check for it being a hot day...
   if nDegreeF > 100 and nDegreeF < 105.8:
      print ("Remember to hydrate!")

   #...check for it being an extremely hot day...
   if nDegreeF > 105.9:
      print ("STAY INSIDE!")
 
   continueYN = input("Input another?")
 
#exit the program
