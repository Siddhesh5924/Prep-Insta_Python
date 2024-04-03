# armstrong_number = input("Enter number to find number is amstrong number or not: ")
#     # take sum variable as 0 for adding power of order numbers to get amstrong number
# sum = 0
# number = int(armstrong_number)
# n = number
# order = len(str(number))
# while (number>0) :
#       digit = number % 10
#       sum += digit **order
#       number = number//10

# if (sum == n):
#         print(f"{n} is amstrong")
# else:
#         print(f"{n} is not amstrong")

# --------------------------------------------------------------------
        # num = int(input("Enter a num: "))
# if num > 0:
#     print("num is +ve")
# else:
#     print("num is -ve")
# --------------------------------

# num = int(input("Enter a num: "))
# if num % 2 == 0:
#     print("num is even")
# else:
#     print('num is odd')
# ------------------------------------------


# n = int(input("Enter a positive integer n: "))
# sum_natural = 0

# if n < 0:
#     print("Please enter a positive integer.")
# else:
#     for i in range(1, n+1):
#         sum_natural += i

#     print("The sum of the first", n, "natural numbers is:", sum_natural)
# ------------------------------------------------------------

# first_num = int(input("Enter a num: "))
# end_num = int(input("Enter a num: "))
# sum = 0
# for i in range(first_num,end_num +1 ):
#     sum = sum + i
# print(f"Sum of numbers between  {first_num} and {end_num} is {sum}"1)
# -------------------------------------------------------------

# Greatest of two nums
# first_num = int(input("Enter a num:"))
# sec_num = int(input("Enter a num:"))
# if first_num > sec_num:
#     print(f"The greater between two nums is {first_num}")
# else:print(f"The greater between two nums is {sec_num}")
# ----------------------------------------------------------------

# Leap year or not
# check_year = int(input("Enter a year"))
# if check_year > 1582:
#     if check_year % 100 == 0 and check_year % 400 == 0:
#         print("Year is leap")
#     if check_year % 4 == 0 and check_year % 100 != 0 :
#         print("year is leap")
#     else:
#         print('not a leap year')
# else:
#     print("Year must be greater than 1582.")
# --------------------------------------------------------------

# count vowels and consonents in str:

# str = input("Enter a str :")
# vowels = 0
# consonents = 0
# for itr in str:
#     if itr in ('a','e','i','o','u','A','E','I','O','U'):
#         vowels+= 1
#     elif itr.isalpha():
#         consonents+=1
# print(f"Vowels:{vowels}, Consonents:{consonents}")
# -----------------------------------------------------

# Remove spaces from str:
# str = input("Enter a str: ")
# result = ''
# for itr in str:
#     if itr!= ' ':
#         result+= itr
# print(result)
# -----------------------------------------------------

# # Fah to cel
# fah = float(input("Enter temp:"))
# # converting Celsius into Fahrenheit
# celsius = ((fah-32)*5)/9
# print(f"Celsius:{celsius:.02f}")
# -----------------------------------------------------

# Smallest among three numbers:
# a = input("enter num:")
# b = input("enter num:")
# c = input("enter num:")

# if a<=b and a<=c:
#     print(f'{a} is smallest')
# elif b<=a and b<=c:
#         print(f'{b} is smallest')
# elif c<=a and c<=b:
#         print(f'{c} is smallest')
# ----------------------------------------------------

# num1 = int(input("enter a num:"))
# num2 = int(input("enter a num:"))
 
# if num1 > num2 :
#     greater = num1
# else:
#     greater = num2
    
# while True:
#     if ((greater % num1 == 0) and (greater % num2 == 0)):
#         break
#     greater += 1
# print("This is answer",greater)

# --------------------------------------------------------

# ar_num = input("Enter a num: ")
# number = int(ar_num)
# num_of_digit = len(str(ar_num))
# n = number 
# sum = 0
# while (number != 0):
#     digits = number % 10 
#     sum = sum + digits ** num_of_digit
#     number //= 10
# if (sum == n):
#     print('Armstrong')
# else:
#     print("Not Armstrong") 
# ------------------------------------------------------

# user_input = input("Enter a num:")
# num = int(user_input)
# if (num % 3 == 0) and (num % 5 == 0):
#         print("FizzBuzz")
# elif num % 5 == 0:
#         print("Buzz")
# elif num % 3 == 0:
#        print("Fizz")
# else:
#     print("It is not a Fizz or Buzz or FizzBuzz")
# ---------------------------------------------------------

# user_input = input("Enter a num\n:")
# sum=digit = 0
# num = int(user_input)
# l = []
# num1=num

# while True:

#     if num == 1:
#         print('No. is happy')
#         break
#     elif num in l:
#         print('Not a happy number')
#         break
#     l.append(num)
#     num1 = num
#     while (num1 != 0):
#         digit = num1 % 10
#         sum += digit ** 2
#         num1 //= 10
#     num =sum

# user_input = int(input("Enter a num : "))
# l = []
# while True:
#     if user_input == 1:
#         print("It's a Happy Number")
#         break
#     elif user_input in l:
#         print('Not a Happy number')
#         break
#     l.append(user_input)
#     num = user_input
#     sum = 0 
#     while(num!=0):
#         digit = user_input % 10
#         sum += digit ** 2
#         user_input//=10
#     user_input = sum



# n = 7 
# n = n**2
# temp1 = n % 10
# temp2 = n // 10
# i = temp1 ** 2 + temp2 ** 2

# while i!=1:
#     if len(str(i))<3:
#         temp1 = i%10
#         temp2 = i//10
#         i = temp1 ** 2 + temp2 ** 2
#         print(f'{temp1} {temp2} {i}', sep = '--')
#     elif len(str(i))==3:
#         temp
    
# -------------------------------------------------------------------

# BACK TO PREP-INSTA

# user_input = input("Enter a year:")
# if user_input.isdigit():
#     year = int(user_input)
#     if year >= 1582:

#         if (year % 100 == 0 and year % 400 == 0):
#            print(f"{year} is a leap year")

#         elif (year % 4 == 0 and year % 100!= 0):
#                 print(f"{year} is a leap year")
#         else:
#              print(f"{year} is not a leap year")
#     else:
#          print("Entered year must be 1582 or later")
# else:
#      print("Invalid input, please enter in numbers")    
# -----------------------------------------------------------------

# PRIME NUMBER
# prime_number = input("Enter a num:")
# if prime_number.isdigit():
#     num = int(prime_number)
#     for itr in range(2, num):
#      if num % itr == 0:
#             sum = False 
#     if sum == 0:
#             print(f"{num} is not a prime number")
#     else:
#             print(f"{num} is a prime number")
# else:
#     print("Invalid input, please enter numbers")        
#---------------------------------------------------------------
# start_num= int(input("enter a num: "))
# end_num = int(input("enter a num:"))
# prime_found = False
# number = start_num
# for itr in range(start_num, end_num+1):
#         if number > 1:
#                 is_prime = True

#                 for itr in range(2, int(number**0.5)+1):
#                         if number % itr == 0:
#                                 is_prime = False
#                                 break
#                 if is_prime:
#                         prime_found = True
#                         print(number, end= ' ')

# OR


# start_range = int(input("enter the start of the range:"))
# end_range = int(input("enter the end of the range:"))

#   #Step 2: Check if the input is correct
# if start_range >= end_range :
#   print(f"Invalid range {start_range} and {end_range}",
#         f"Entered end range must be greater than start_range.")

#   exit()

#     # Step 3: Initialize the number variable to start a flag to check if
#     # any prime number if found

# prime_found = False
# number = start_range

#   # Print the prime within the range

# print(f"The prime numbers within the range {start_range:02d} and {end_range:02d}")

#   # Step 4 For loop to check if the number within the range

# for number in range(start_range, end_range + 1):
#     if number > 1:
#       is_prime = True

#   # Step 5: Nested for loop to check to variable number is prime
#           # Logic used is starting from 2 till sqrt of variable number
#           # Check the module. If remainder is 0 the number is prime\
#       for divisor in range(2, int(number ** 0.5) + 1):
#         if number % divisor  == 0:
#           is_prime = False
#           break
#       if is_prime:
#           prime_found = True
#           print(number, end = ' ')
# ________________________________________________________________________
          
# SUM OF DIGITS OF A NUMBER
# num = int(input("enter a num:"))
# sum_of_digits = 0
# while num > 0:
#     digit = num % 10
#     sum_of_digits+= digit
#     num //= 10
# print(sum_of_digits)
# --------------------------------------------------------------------

# REVERSE A NUMBER
# reverse_num = int(input("enter a num: "))
# sum = 0
# while reverse_num != 0:
#     digit = reverse_num % 10
#     sum = sum * 10 + digit
#     reverse_num //= 10
# print(f"Reversed num is{sum}")
# --------------------------------------------------------------------

# PALINDROME NUMBER

# pal_no = input("ENter a num") 
# str = ''
# for itr in pal_no:
#     str = itr + str
# if pal_no == str:
#     print("Amrstrong")
# else:
#     print("Not armstrong")
# ------------------------------------------------------------------

# ARMSTRONG NUMBER
# ar_num = input("Enter a num:")
# sum = 0
# number = int(ar_num)
# n = number
# num_of_digits = len(str(number))
# while number > 0:
#     digit = number % 10
#     sum += digit **num_of_digits
#     number//= 10
# if (sum == n):
#     print()
# ----------------------------------------------------------

# Armstrong Numbers in Given Range:

# ar_num1 = int(input('Enter a num:'))
# ar_num2 = int(input('Enter a num:'))

# for itr in range(ar_num1, ar_num2 + 1):
#     num_of_digits = len(str(itr))
#     sum = 0
#     temp = itr
#     while temp > 0 :
#         digit = temp % 10
#         sum = sum + digit ** num_of_digits
#         temp //= 10
#     if itr == sum:
#         print(itr)
# -----------------------------------------------------------

# FIBONACCI SERIES less than 10
# fib_num = int(input("Enter a num"))
# temp = int(fib_num)
# prev, current = 0,1
# sum = 0
# print(prev, current, end = ' ')
# for itr in range(1,fib_num):
#         sum = prev + current
#         prev = current
#         current = sum
#         if fib_num <= sum:
#                 break
#         print(sum, end =" ")
# ----------------------------------------------------------

# FIBONACCI SERIES UPTO nth term
# fib_num = int(input("enter a num: "))
# prev, current = 0,1
# sum = 0 
# print(prev,current,end=' ')
# for itr in range (1, fib_num):
#         sum = prev + current
#         prev = current
#         current = sum
#         print(sum,end = ' ')


# HARMONIC NUMBER

# har_num = int(input("enter a num:"))
# sum = 0 
# for itr in range(1,har_num+1):
#     sum += 1/itr
# print(f"{sum:.02f}")

# # Input the value of n
# n = int(input("Enter the value of n: "))

# # Initialize the sum of harmonic numbers
# harmonic_sum = 0

# # Iterate from 1 to n
# for i in range(1, n + 1):
#     # Add the reciprocal of the current number to the sum
#     harmonic_sum += 1 / i

# # Print the sum of harmonic numbers
# print(f"The sum of the first, {n} harmonic numbers is: {harmonic_sum:.02f}")


# ---------------------------------------------------------------------------------------

#FACTORS of a Number

# number = input("Enter a num")
# num = int(number)
# sum = 0
# for itr in range(1,num):
#     if num % itr == 0:
#         print(itr, end = " ")

# ----------------------------------------------------------------------

#PRIME FACTORS OF A NUMBER
# number = input("Enter num:")
# num = int(number)
# sum = []
# for itr in range(1, num):
#     if num % itr ==0:
#         is_prime = True
#         for prime in range(2, (itr//2+1)):
#             if itr % prime == 0:
#                 is_prime = False
#         if is_prime:
#             print(itr, end = ' ') 
# ----------------------------------------------------------------------

# STRONG NUMBER
# def factorial(n):
#     ans = 1
#     for itr in range(1, n+1):
#         ans = itr * ans
#     return ans
 
# number = int(input("Enter a num: "))
# sum = 0
# temp = number 
# while (number > 0):
#     digit = number % 10
#     sum = sum + factorial(digit)
#     number//=10
# if sum == temp:
#     print("Strong")
# else:
#     print("Weak")
# ------------------------------------------------------------------------------
    
# def fibonacci(n):
#     prev,current = 0,1
#     sum = 0
#     print(prev,current, end =' ')
#     for itr in range(1,n):
#         sum = prev + current
#         prev = current
#         current = sum 
#         print(current,end = " ")
# fibonacci(5)
# ------------------------------------------------------------------------------
# def prime(n):
#     is_prime = True
#     for itr in range(2,n):
#         if n % itr == 0:
#             is_prime = False
#     return is_prime
# print(prime(9))
# -----------------------------------------------------------------------------

# FACTORIAL of a number
# def factorial(n):
#     sum = 1
#     for itr in range(1,n+1):
#         sum = sum * itr
#     return sum
# ans = factorial(5)
# print(ans)
# --------------------------------------------------------------

# PERFECT NUMBER
# def perfect(n):
#     temp = n
#     sum = 0
#     for itr in range(1,n):
#         if temp % itr == 0:
#             print(itr, end = ' ')
#             sum = sum +itr
#     if sum == temp:
#         return True
#     else:
#         return False 
# ans = perfect(6)
# print(ans, end = ' ')

# ------------------------------------------------------------------

# # ARMSTRONG NUMBER
# def armstrong(n):
#     sum = 0
#     temp = n
#     order = len(str(n))
#     while temp > 0:
#         digit = temp % 10 
#         sum = sum + digit ** order
#         temp//= 10
#     if n == sum:
#         return True
#     else:
#         return False
# ans = armstrong(153)
# print(ans)
# --------------------------------------------------------------------
# def number(n):
#     if n > 0 :
#         return True
#     else:
#         return False
# ans = number(6)
# print(ans)
#----------------------------------------- 

# array = [5,542,50,3,52,2]
# max = array[0]
# for i in range(1, len(array)):
#     if max > array[i]:
#         max = array[i]
# print(max)
    
# ------------------------------------------

# arr = [5,542,50,3,52,2]
# sum = 0
# for i in range(len(arr)):
#     sum = sum + arr[i]
# print(sum)
# ---------------------------------------------

# rev_num = int(input("Num: "))
# sum = 0
# while rev_num !=0:
#     digit = rev_num % 10
#     sum = sum*10+digit
#     rev_num//=10
# print(sum)
# ------------------------------------------------
# fact_num = input("ENter num:")
# fact = int(fact_num)
# sum = 1
# for i in range(1, fact+1):
#     sum = sum * i
# print(f"factorial of {fact_num} is {sum}")

# =-------------------------------------------------
# rev_num = '12345'
# str = ""
# for i in rev_num:
#     str = i+str  
# print(str)
# ------------------------------

# # Harmonic num
# num = 5
# sum = 0
# for i in range(1,5+1):
#     sum+=1/i
# print(f"{sum:.02f}")
# ---------------------------------------------------------
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#   greater = num1
# else:
#   greater = num2
# while(True):
#   if((greater % num1 == 0) and (greater % num2 == 0)):
#       lcm = greater
#       break
#   greater += 1
# print("LCM of",num1,"and",num2,"=",greater)


        
        
        
             
                


    

        
    



