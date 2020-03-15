# from-scratch
Data science from scratch by Joel Grus

Various functions defined in the begining of the book has been refered to in the subsequent chapters without explicitly mentioning these. Therefoer, I have created libraris on the most commmonly used functions so that these could be used freely without retyping these functions into individual notebooks. 

To create a library of functions, you have to create a directory in Linux and and create a special file with the name __init__.py in it. All the functions defined in this __init__.py file will be available in notebook where it is imported 

e.g. if we create a new library (directory) with the name myLib and place a function called vector_add(x,y) in the __init__.py file under myLib directory, we can simply say import myLib in a notebook and vector_add() function will become available in the notebook
