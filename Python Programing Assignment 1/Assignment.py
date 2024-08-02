# Q1:
"""
Age Assignments Based on the Riddle

Problem Statement: Write a program to solve this age-related riddle! Talha, Azfar, Tariq,Tahir, and Akram are all friends. Their ages are as follows:
Talha is 21 years old.
Azfar is 6 years older than Talha.
Tahir is 20 years older than Azfar.
Tariq is as old as Talha's age plus Azfar's age.
Akram is the same age as Tahir.
Your code should store each person's age to a variable and print their names and ages at the end."""
# Solution:
talha_age:int = 21
azfar_age:int = talha_age + 6
tahir_age:int = azfar_age + 20
tariq_age:int = talha_age + azfar_age
akram_age:int = tahir_age

print(f"Talha is {talha_age} years old.")
print(f"Azfar is {azfar_age} years old.")
print(f"Tahir is {tahir_age} years old.")
print(f"Tariq is {tariq_age} years old.")
print(f"Akram is {akram_age} years old.\n")

# Q2:
"""
Formatted String Interpolation

Task: Given the variables name, age, and city, use f-strings to construct a sentence that describes a person using these variables.
name:str = "Alice"
age:int = 30
city:str = "New York"
Instructions: Use an f-string to create a sentence in the format: "Alice is 30 years old and lives in New York."
Expected Output:
Alice is 30 years old and lives in New York."""
# Solution:
name:str = "Talha"
age:int = 20
city:str = "Lahore"
sentence:str = f"{name} is {age} years old and lives in {city}."
print(sentence)

# Q3:
"""
String Manipulation

Task: Given the string s, use string methods to:
Capitalize the first letter: make the first character uppercase and the rest of the string lowercase.
Convert to uppercase: change all characters in the string to uppercase.
Convert to lowercase: change all characters in the string to lowercase.
s:str = "hElLo WoRlD"
Expected Output:
Hello world
HELLO WORLD
hello world"""
# Solution:

s:str = "hElLo WoRlD"
# Capitalize the first letter
capitalized_first_letter:str =s.capitalize()
print(f"\n{capitalized_first_letter}")
# Convert to uppercase
uppercase:str = s.upper()
print(uppercase)
# Convert to lowercase
lowercase:str = s.lower()
print(f"{lowercase}\n")

# Q4:
"""
Substring Search

Task: Given the string s, use string methods to:
Find the index of "fox": get the starting index of the substring "fox". If "fox" is not found, it should return -1.
Count occurrences of "the": Use the string's built-in method to count how many times the substring "the" appears in the string.
s:str ="the quick brown fox jumps over the lazy dog"
Expected Output:
index of 'fox' is 16
'the' appears 2 times
"""
# Solution:
s_:str ="the quick brown fox jumps over the lazy dog"
index=s_.find("fox")
print(f"index of 'fox' is {index}")
#Count occurrences
word_to_count:str="the"
count_occurrences=s_.count(word_to_count)
word=count_occurrences
if(word):
  print(f"{word_to_count} appears {count_occurrences} times.\n")
else:
  print("Word not Found\n")
  
  # Q5:
  """
  String Replacement

Task: Given the string s, use string methods to:
Replace "Python" with "Java": substitute "Python" with "Java".
s:str ="I love programming in Python"
Expected Output:
I love programming in Java
  """
# Solution:
text:str ="I love programming in Python"
new_text:str=text.replace("Python","Java")
print(f"{new_text}\n")

# Q6:
"""
String Splitting and Joining

Task: Given the string s, use string methods to:
Split into a list: break the string into a list of substrings based on the delimiter ,.
Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
s:str ="apple,banana,cherry,dates"
Expected Output:
["apple", "banana", "cherry", "dates"]
apple banana cherry dates
"""
# Solution:
words:str ="apple,banana,cherry,dates"
split_string:list[str]=words.split(",")
print(split_string)
new_words:str=" ".join(split_string)
print(f"{new_words}\n")

# Q7:
"""
String Stripping and Justifying

Task: Given the string s, use string methods to:
Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
s:str ="   Python is fun!   "
Expected Output:
Python is fun!
Python is fun!*****
*****Python is fun!
"""
# Solution:
whitespace:str ="   Python is fun!   "
remove_whitespaces:str=whitespace.strip()
Left_justify:str=remove_whitespaces.ljust(20,'*')
Right_justify:str=remove_whitespaces.rjust(20,'*')
print(remove_whitespaces)
print(Left_justify)
print(f"{Right_justify}\n")

# Q8:
"""
Convert an integer to its binary representation

Task: Given an integer num
Obtain the binary representation of num
num:int = 45
Expected Output:
Binary representation : 0b101101"""
# Solution:
num:int = 45  

binary_representation:str = bin(num)

print(f"Binary representation : {binary_representation}\n")

# Q9:
"""
Calculate Powers of Numbers.

Task: Given two integers base and exponent
Compute base raised to the power of exponent.
base:int = 3
exponent:int = 4
Expected Output:
Power result: 81"""
# Solution:
base:int = 3
exponent:int = 4
power_result:int = base ** exponent
print(f"Power result: {power_result}\n")

# Q10:
"""
Round floating-point numbers

Task: Given a floating-point number value
Round value to the nearest integer.
Round value to two decimal places.
value:float = 12.34567
Expected Output:
Rounded to nearest integer: 12
Rounded to two decimal places: 12.35"""
# Solution:
value:float = 12.34567

rounded_integer:int = round(value)
rounded_to_two_decimal_places:float = round(value, 2)

print(f"Rounded to nearest integer: {rounded_integer}")

print(f"Rounded to two decimal places: {rounded_to_two_decimal_places}\n")