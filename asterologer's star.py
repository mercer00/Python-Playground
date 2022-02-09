print("Astrologer's Star!")
print("First value is the number of rows")
print("Second value represents the sequence , 0 - Descending order and 1 - Ascending order")

asterix = "*"
while True:
    user_rows = int(input(">>> "))
    user_sequence = bool(int(input(">> ")))
    if user_sequence == True:
        for i in range(1 , user_rows+1):
            print(i * asterix)
    if user_sequence == False:
        for i in range(user_rows , 0 , -1):
            print(i * asterix)
    print()
