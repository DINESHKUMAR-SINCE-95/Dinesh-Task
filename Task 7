Here is the Python program that accomplishes the tasks mentioned:

```python
import os
from datetime import datetime

# Function to create a text file with the current timestamp as its content
def create_timestamp_file():
    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # Define the file name using the timestamp
    file_name = f"{timestamp}.txt"
    # Write the timestamp to the file
    with open(file_name, 'w') as file:
        file.write(timestamp)
    print(f"File '{file_name}' created with content: {timestamp}")

# Function to read from a text file and display its content
def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of the file '{file_name}':\n{content}")
    else:
        print(f"File '{file_name}' does not exist.")

# Example usage:
create_timestamp_file()  # This will create a file with the current timestamp

# To read the file, use the read_file function with the name of the created file
# For example, if the created file is '2023-07-12_10-30-45.txt':
# read_file('2023-07-12_10-30-45.txt')
```

### Explanation:

1. **Creating a Timestamp File:**
   - The `create_timestamp_file` function retrieves the current timestamp and formats it.
   - The function then creates a file named with this timestamp and writes the timestamp as its content.
   - Finally, it prints a message indicating that the file was created and shows its content.

2. **Reading from a File:**
   - The `read_file` function checks if the specified file exists.
   - If the file exists, it reads the content and prints it to the console.
   - If the file does not exist, it prints a message indicating the file does not exist.

### Note:
- The `create_timestamp_file` function creates a new file with a unique name based on the current timestamp each time it is called.
- You need to pass the correct file name to the `read_file` function to read the content. The example usage provided demonstrates how to use these functions.
