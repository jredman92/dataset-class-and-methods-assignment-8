"""
Lab Assignment 8: Dataset Class
Submitted by Jaymie Redman
Submitted: November 16, 2025

Assignment 8: This project defines a class to manage temperature data. It
includes placeholder methods for loading data, calculating statistics, and
tracking the number of TempDataset objects created. A unit test is provided to
verify the class and methods work as expected.

Assignment 7: This assignment introduces two methods (in detail).
print_filter() - prints a list of sensors that are active and inactive.
change_filter() - allows a user to activate a sensor or deactivate it.
The change_filter() is initiated through the menu prompt #3 choice.
The change_filter() method will print the filter list showing active or
inactive states, and it will allow the user to turn a sensor on or off.

Assignment 6: Bubble sort a sensor list but using recursion. Use a test case
as provided (similar to assignment 5, but with reference to the sensor list
information from assignment 4).

Assignment 5: A separate recursion assignment (as another project; see
assignment 5)

Assignment 4: Creating a Sensor List and Filter List using a dictionary and
list comprehensions.

Assignment 3: Adds a menu interface for the user, which prompts them to select
different options.

Assignment 2: This assignment adds code to prompt the user for a temperature
in Celsius and then converts that temperature to a specified different
temperature unit.

Assignment 1: This program demonstrates printing lines of text to the screen
"""


class TempDataset:
    temp_dataset_value = 0
    
    def __init__(self):
        """Initialize a new TempDataset object."""
        self._data_set = None
        self._name = "Unnamed"
        TempDataset.temp_dataset_value += 1
   
    @property
    def name(self):
        """Return the current name."""
        return self._name
    
    @name.setter
    def name(self, new_name):
        """Set a name if it meets length requirements."""
        if 3 <= len(new_name) <= 20:
            self._name = new_name
        else:
            raise ValueError("Too short or too long")
        
    def process_file(self, filename):
        """Placeholder for loading file."""
        return False
    
    def get_summary_statistics(self, filter_list):
        """Return summary stats."""
        return None

    def get_avg_temperature_day_time(self, filter_list, day, time):
        """Return average temperature of day/time."""
        return None
    
    def get_num_temps(self, filter_list, lower_bound, upper_bound):
        """Return a count of temperatures."""
        return None
    
    def get_loaded_temps(self):
        """Return loaded temperatures."""
        return None

    @classmethod
    def get_num_objects(cls):
        """Return total number of TempDataset objects created."""
        return cls.temp_dataset_value
        

def main():
    """Run the program"""
    
    
if __name__ == "__main__":
    main()
    
    
    
"""Unit Test"""
current_set = TempDataset()

print("First test of get_num_objects: ", end='')

if TempDataset.get_num_objects() == 1:
    print("Success")
else:
    print("Fail")

second_set = TempDataset()

print("Second test of get_num_objects: ", end='')

if TempDataset.get_num_objects() == 2:
    print("Success")
else:
    print("Fail")

print("Testing get_name and set_name: ")

print("- Default Name:", end='')

if current_set.name == "Unnamed":
    print("Success")
else:
    print("Fail")

print("- Try setting a name too short: ", end='')

try:
    current_set.name = "to"
    print("Fail")
except ValueError:
    print("Success")

print("- Try setting a name too long: ", end='')

try:
    current_set.name = "supercalifragilisticexpialidocious"
    print("Fail")
except ValueError:
    print("Success")

print("- Try setting a name just right (Goldilocks): ", end='')


try:
    current_set.name = "New Name"
    if current_set.name == "New Name":
        print("Success")
    else:
        print("Fail")
except ValueError:
    print("Fail")

print("- Make sure we didn't touch the other object: ", end='')
if second_set.name == "Unnamed":
    print("Success")
else:
    print("Fail")

print("Testing get_avg_temperature_day_time: ", end='')
if current_set.get_avg_temperature_day_time(None, 0, 0) is None:
    print("Success")
else:
    print("Fail")

print("Testing get_num_temps: ", end='')
if current_set.get_num_temps(None, 0, 0) is None:
    print("Success")
else:
    print("Fail")

print("Testing get_loaded_temps: ", end='')
if current_set.get_loaded_temps() is None:
    print("Success")
else:
    print("Fail")

print("Testing get_summary_statistics: ", end='')
if current_set.get_summary_statistics(None) is None:
    print("Success")
else:
    print("Fail")

print("Testing process_file: ", end='')
if current_set.process_file(None) is False:
    print("Success")
else:
    print("Fail")


r"""
C:\Users\jredm\PycharmProjects\PythonProject\.venv\Scripts\python.exe C:\Users\jredm\PycharmProjects\PythonProject\Assignments\assignment_8.py
First test of get_num_objects: Success
Second test of get_num_objects: Success
Testing get_name and set_name:
- Default Name:Success
- Try setting a name too short: Success
- Try setting a name too long: Success
- Try setting a name just right (Goldilocks): Success
- Make sure we didn't touch the other object: Success
Testing get_avg_temperature_day_time: Success
Testing get_num_temps: Success
Testing get_loaded_temps: Success
Testing get_summary_statistics: Success
Testing process_file: Success

Process finished with exit code 0
"""