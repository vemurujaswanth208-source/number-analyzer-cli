while True:

    print("number analyzer")
    print("1.analyzer number")
    print("2.exit")

    choice = input("enter your choice: ")

    if choice == "1":

        num = int(input("enter a number: "))

        digits = 0 
        sum = 0 
        even_count = 0 
        odd_count = 0 
        largest = 0

        temp = num ## just to keep original number 
                   #safe this i learnt from my past small project

        while temp > 0:

            last = temp % 10

            digits += 1

            sum = sum + last

            if last % 2 == 0:
                even_count += 1
            else:
                odd_count += 1 

            if last > largest:
                largest = last  

            temp = temp // 10 

        print("\nResults:")
        print("Digits:", digits)
        print("Sum:", sum)
        print("Even:", even_count)
        print("Odd:", odd_count)
        print("Largest digit:", largest)

    elif choice == "2":
        print("exiting")
        break
   
    else:
        print("invalid choice,try again")

        