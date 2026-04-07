
#Create another file called main.py:
import mymodule
result = mymodule.add(10, 5)         # Call one function from the module
print("Addition Result:", result)           # Addition Result: 15
# Call another function
print(mymodule.greet("Alice"))           # Hello, Alice!