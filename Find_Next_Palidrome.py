# Take Input From User In (Int) To Set limit of input to find palidrome number.
m =int(input ("Enter the number to find palidrome limit \n"))

limit = 0
# Whiile loop For Limits complete and break the program
while limit< m:

    #Here I'm Making a function  nex take arugment num

    def nex (num):
        #we are casting int(num) to str(num) store in numstr
        numstr = str(num)

        for i in range(num+1, 9000000000):
        # Here we Are Make A Range Define To 90000000000 From num+1
            # print(i)
            if numstr == numstr[::-1]:
                #Her We Check The Condition  if numstr == reverse of numstr[::-1]
                return f"Number Is Already Palidrome {num}"
                #Here We Are Printing Condition Results
            elif str(i ) == str(i)[::-1]:
                #here we are check condition of str(i) == reverse of str(i)
                return f"Next Palidrome is {i}\n"
                #here we are print the results


    print(nex(input("Enter the Number  \n")))
    #here We are Take input
    limit = limit+1
