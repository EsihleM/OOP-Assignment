# OOP-Assignment
# README
## Description

This project contains a Python script that demonstrates the concept of inheritance in Object-Oriented Programming (OOP). It defines a `Person` class and a `Dancer` class that inherits from `Person`.

## Classes

- **Person**: Represents a person with attributes `name` and `age`, and a method `introduce` to print a self-introduction.
- **Dancer**: Inherits from `Person` and adds an additional attribute `dance_style` and a method `dance` to print a message about the dance style.

##Usage
1. Create an instance of the `Person` class and call the `introduce` method.
2. Create an instance of the `Dancer` class and call both the `introduce` and `dance` methods.

## How to Run

1. Ensure you have Python installed on your system.
2. Save the code in a file named oop.py.
3. Open a terminal and navigate to the directory containing oop.py.
4. Run the script using the command:
   ```bash
   python oop.py
   ```
## Notes

- The `Dancer` class uses the `super()` function to call the `__init__` method of the `Person` class.
