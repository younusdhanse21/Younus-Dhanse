
# PYTHON EXCEPTION HANDLING – 25 PRACTICE EXAMPLES
# Topics Covered:
# Errors vs Exceptions,
# Try-Except,
# Finally,
# Raising Exceptions

# ---

# 1. Handle division by zero

# ---
print(10/0)
try:
    a = 10
    b = 0
   
except:
    print("Division by zero error")

---

2. Handle invalid number input

---

try:
num = int(input("Enter number: "))
print(num)
except:
print("Invalid input")

---

3. Catch ZeroDivisionError specifically

---

try:
x = 20
y = 0
print(x/y)
except ZeroDivisionError:
print("Cannot divide by zero")

---

4. Handle multiple exceptions

---

try:
    a = int(input("Enter number: "))
    print(10/a)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")

---

5. Use finally block

---

try:
    x = int(input("Enter number: "))
    print(10/x)
except:
    print("Error occurred")
finally:
    print("Program finished")

---

6. Handle list index error

---

list1 = [1,2,3]
print(list1[5])



try:
    list1 = [1,2,3]
    print(list1[5])
except IndexError:
    print("Index out of range")

---

7. Handle file not found

# ---
f = open("data.txt")


try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found")

---

8. Use Exception as variable

---

try:
    a = int(input())
    print(5/a)
except Exception as e:
    print("Error descrip is this -:", e)

# ---

9. Try without error

# ---

try:
    print("Hello)
    print(2/0)
   
except:
    print("Error")

# ---

10. Use finally with file

---

try:
    f = open("test.txt")
except:
    print("File error")
finally:
    print("Closing program")

---

11. Raise custom exception

---

age = int(input("Enter age: "))
if age < 18:
    raise Exception("Not eligible")

---

12. Raise error for negative number

---

num = int(input())
if num < 0:
raise Exception("Negative number not allowed")

---

13. Handle ValueError

---

try:
n = int(input("Enter number: "))
except ValueError:
print("Enter valid integer")

---

14. Try with string conversion

---

try:
x = int("abc")
except:
print("Conversion error")

---

15. Nested try block

---


for i in range(4):
    for j in range(2):
        print(i,j)





try:
    a =int(input("enter a number: "))
    try:
        print(10/0)
    except ZeroDivisionError:
        print("Inner exception handled")

except:
    print("Outer exception")

---

16. Try with list input

---

try:
arr = [10,20,30]
print(arr[10])
except:
print("Invalid index")

---

17. Try with dictionary

---

try:
    data = {"a":10}
    print(data["b"])
except KeyError:
    print("Key not found")

---

18. Use finally after division

---

try:
a = int(input())
print(100/a)
except:
print("Error")
finally:
print("Execution complete")

---

19. Handle type error

---

try:
    print("2" + 5)
except TypeError:
    print("Type mismatch")

---

20. Exception for password check

---

password = input("Enter password: ")

if len(password) < 6:
raise Exception("Password too short")

---

21. Try with float conversion

---

try:
num = float(input())
print(num)
except:
print("Invalid float value")

---

22. Divide numbers from list

---

try:
numbers = [10,20,0]
print(100/numbers[2])
except ZeroDivisionError:
print("Zero division error")

---

23. Handle multiple errors together

---

try:
a = int(input())
b = int(input())
print(a/b)
except (ValueError, ZeroDivisionError):
print("Invalid input or division by zero")

---

24. Raise exception for marks

---

marks = int(input("Enter marks: "))

if marks > 100:
raise Exception("Marks cannot exceed 100")

---

25. Complete example

---

try:
num = int(input("Enter number: "))
if num < 0:
raise Exception("Negative number not allowed")
print(50/num)
except ZeroDivisionError:
print("Cannot divide by zero")
except Exception as e:
print(e)
finally:
print("Program ended")
