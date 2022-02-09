import random
periodic_table = {"Phosphorus" : 15 , "Sulphur" : 16 , "Chlorine" : 17 , "Argon" : 18 , "Potassium" : 19 , "Calcium" : 20}
atom_list = list(periodic_table.keys())


while True:
    atom = random.choice(atom_list)
    answer = periodic_table[atom]
    print(f"What is the atomic number of {atom}? : " , end="")
    user_input = int(input())

    if user_input == answer:
        print("Correct!!")
    else:
        print(f"Wrong.. , The answer is {answer}")
