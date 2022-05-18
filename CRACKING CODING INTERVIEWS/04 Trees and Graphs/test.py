# Sum numbers from a to b
import os

l = os.listdir('D:\Ciro\OneDrive\Bibliografia\META\Coding Exercises\Trees and Graphs/')
print(l)
for n in l:
    new_name = n.replace(' ', '_').replace('_4.', '_4_')
    os.rename('D:\Ciro\OneDrive\Bibliografia\META\Coding Exercises\Trees and Graphs/' + n,
              'D:\Ciro\OneDrive\Bibliografia\META\Coding Exercises\Trees and Graphs/' + new_name)


