# num-cousin
This Python code was made with the following logic:

• Create two "in range" loops with limit given by the user 

• Divide each number by each one in the range
  Ex: 1/1 1/2 1/3 until the "divisor" range ends to then proceed to the next number in "cousin" range
  This considering that both loops will have the same range, shows the slowest part of the code

• Begin filtering cousin numbers by two parts
  1: Create a "if" logic where if the division of the two loops result in a integer executes the next filtering part
  
  2: Here it gets tough, create a "if" that only accepts if the declared variable is "1" and then turns it to zero, else it adds up 1 to the variable
     I made it in order to only accepts odd numbers, but 2, since all even numbers are divisible by "2"
     Then the next "if" will filter only numbers that are equal to it's divisor and will print the cousin number with order defined
     The break then happens and the loop repeat
     
• This may not be a great project, but I was happy to make it, and that's all I have to say about this code
