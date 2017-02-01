How to run this program (HW1_E.py):
1. Execute the following terminal command: 'python HW1_e.py <min_support> <input_file_name>'
   where: min_support      is an integer value (ex: 2, 3, etc.)
          input_file_name  is the name of the input file containing transaction database (ex: input.txt)

   An example command to execute this program is: 
       python HW1_e.py 2 input.txt

   An example output to the above command is: 
       Min Threshold     :  2
			 Input File        :  input.txt

			 Finding all frequent patterns in the file...

			 Frequent patterns :  ['a', 'c', 'b', 'p', 'r', 'ac', 'ab', 'cb', 'cr', 'acb']

2. The input file (in this case: input.txt) should follow the following format:
	     a) each line represents one transaction
	     b) each line has comma separated items, which represent all the items in a particular transaction

	 An example of the input.txt would be the following:
	     c,r,a
			 p,b
			 r,c,b
			 p,c,a
			 a,b,s,c
			 t,a,b,c

