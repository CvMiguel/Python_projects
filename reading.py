def read_log_file(log_filename):
    try:
        with open(log_filename, 'r') as log_file:
            # Read all lines from the log file
            lines = log_file.readlines()

            # Assuming you want the first line (you can adjust this)
            specific_line = lines[0].strip()  # Remove leading/trailing whitespace
            return specific_line
    except FileNotFoundError:
        print(f"Log file '{log_filename}' not found.")
        return None

def extract_number_from_line(line):
    # You'll need to adjust this based on the actual format of your log line
    # For example, if the number is always at the end of the line:
    # number = float(line.split()[-1])
    # Or use regular expressions to extract the number
    # Example: import re; number = float(re.search(r'\d+', line).group())
    pass

def read_data_file(data_filename):
    # Read numbers from the data file (similar to reading log file)
    pass

def calculate_average(numbers):
    # Compute the average
    pass

def main():
    log_filename = input("Enter the log file name: ")
    specific_line = read_log_file(log_filename)
    if specific_line:
        number = extract_number_from_line(specific_line)

        data_filename = input("Enter the data file name (e.g., data.txt): ")
        data_numbers = read_data_file(data_filename)

        if data_numbers:
            all_numbers = [number] + data_numbers
            average = sum(all_numbers) / len(all_numbers)
            print(f"Calculated average: {average:.2f}")

            # Write the average back to the log file or another .txt file
            # You can implement this part based on your requirements
        else:
            print(f"No valid data found in '{data_filename}'.")
    else:
        print(f"No specific line found in '{log_filename}'.")

if __name__ == "__main__":
    main()
