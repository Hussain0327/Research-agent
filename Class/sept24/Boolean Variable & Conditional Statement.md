1. Boolean Variable
In Python, a boolean variable is a data type that can hold one of two values: True or False. These values are used to represent the truth values in logical operations and conditions.

Boolean Values:

True: Represents a condition that is correct or valid.
False: Represents a condition that is incorrect or invalid.
Assigning Boolean Variables: Boolean variables can be created by assigning True or False to a variable:

is_sunny = True
is_raining = False
Booleans are essential for controlling logic in Python programs, allowing you to make decisions based on conditions.

2. Relational Operations
In Python, relational operations are used to compare two values. These operations return a boolean value (True or False) based on the comparison.

Here’s a chart of the relational operations in Python:

Operator	Description	Example	Result
==	Equal to	5 == 5	True
!=	Not equal to	5 != 3	True
>	Greater than	7 > 3	True
<	Less than	3 < 7	True
>=	Greater than or equal to	7 >= 7	True
<=	Less than or equal to	3 <= 7	True
These operators compare the values on either side and return True or False.

3. Logical Operations

[ ]

Start coding or generate with AI.
Logical operations in Python are used to combine multiple conditions or expressions, and they return a boolean value (True or False) based on the logic applied. They help build more complex conditions, making it easier to perform decision-making in Python programs. Python supports three logical operators: and, or, and not. Here’s a breakdown of each:

and Operator: This operator returns True if both expressions on either side of it are True. If one or both expressions are False, the result will be False.

condition1 and condition2
(5 > 3) and (10 < 20)  # True, because both conditions are true
(5 > 3) and (10 > 20)  # False, because the second condition is false
or Operator: This operator returns True if at least one of the expressions is True. It returns False only when both expressions are False.

condition1 or condition2
(5 > 3) or (10 < 20)   # True, both conditions are true
(5 > 3) or (10 > 20)   # True, because the first condition is true
(5 < 3) or (10 > 20)   # False, both conditions are false
not Operator: The not operator negates the boolean value of the expression it precedes. If the expression is True, not makes it False, and vice versa.

not condition
not (5 > 3)  # False, because 5 > 3 is True, and not inverts it
not (5 < 3)  # True, because 5 < 3 is False, and not inverts it
Truth Table
Expression 1	Expression 2	Expression 1 and Expression 2	Expression 1 or Expression 2
True	True	True	True
True	False	False	True
False	True	False	True
False	False	False	False
4. Conditional Statements in Python
In Python, the program executes statements line by line, from top to bottom, in the order they appear. This is the most basic form of program execution. However, sometimes we need to execute specific statements based on a condition. Conditional statements are used to run certain blocks of code depending on whether a condition is True or False. The most commonly used conditional statements are if, elif (short for "else if"), and else, which help control the flow of the program based on different conditions.

if Statement:
The if statement is used to test a condition. If the condition evaluates to True, the block of code inside the if statement is executed.

if condition:
    # code to execute if condition is True
age = 18
if age >= 18:
    print("You are an adult.")
Note that,

The condition is created using relational or logical operators (==, !=, <, >, <=, >=, and, or, etc.).
Python uses colons (:) after the conditional expression.
code to execute if condition is true is indented.
elif Statement:
The elif statement allows you to check multiple conditions. If the first if condition is False, the program checks the elif condition(s).

if condition1:
    # code if condition1 is True
elif condition2:
    # code if condition1 is False and condition2 is True
age = 15
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else Statement:
The else statement executes a block of code when none of the if or elif conditions are True.

if condition1:
    # code if condition1 is True
elif condition2:
    # code if condition2 is True
else:
    # code if both conditions are False
age = 10
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
5. Nested Conditionals
Nested conditionals in Python refer to placing one conditional statement inside another. This allows you to check multiple conditions and take actions depending on more complex logical scenarios. Essentially, it means using if, elif, or else inside another if statement.

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("You are too young to vote.")
Here:

The outer if checks if age is greater than or equal to 18.
If True, the nested if checks if citizen is True.
Depending on these conditions, different messages are printed.
6. String Comparison
In Python, string comparison is performed lexicographically based on Unicode values, with characters compared from left to right. The comparison is case-sensitive, meaning uppercase letters are considered smaller than lowercase ones. If two strings share a common prefix, the shorter string is considered smaller.

Following is a concise table showing selected uppercase and lowercase letters with their Unicode values to illustrate how Python compares strings:

Character	Unicode Value
'A'	65
'B'	66
'Z'	90
'a'	97
'b'	98
'z'	122
This shows that all uppercase letters come before lowercase letters in Unicode, which affects lexicographic string comparison in Python.


[ ]
x="A"
y="a"
print(x<y)
True