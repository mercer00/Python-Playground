import random
periodic_table = {"Hydrogen" : 1 , "Helium" : 2 , "Lithium" : 3 , "Beryllium" : 4 , "Boron" : 5 , "Carbon" : 6 , "Nitrogen" : 7 , "Oxygen" : 8 , "Flourine" : 9 , "Neon" : 10 , "Sodium" : 11 , "Magnesium" : 12 , "Aluminium" : 13 , "Silicon" : 14 , "Phosphorus" : 15 , "Sulphur" : 16 , "Chlorine" : 17 , "Argon" : 18 , "Potassium" : 19 , "Calcium" : 20}
atom_list = list(periodic_table.keys())



atom = random.choice(atom_list)
answer = periodic_table[atom]
print(f"What is the atomic number of {atom}? : " , end="")
user_input = int(input())

if user_input == answer:
    print("Correct!!")
else:
    print(f"Wrong.. , The answer is {answer}")
