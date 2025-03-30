import csv

def read_csv(file_path):
    """Reads a CSV file and returns its content as a list of lists."""
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = [row for row in reader]  # Store all rows in a list
    return data

def get_column_widths(data):
    """Finds the maximum width needed for each column."""
    column_widths = []
    for col in zip(*data):  # Transpose rows into columns
        max_width = max(len(str(item)) for item in col)  # Find the longest item
        column_widths.append(max_width)
    return column_widths

def print_table(data):
    """Prints a formatted table with borders."""
    col_widths = get_column_widths(data)
    total_width = sum(col_widths) + len(col_widths) * 3 + 1  # Calculate table width
    
    def print_separator():
        print("+" + "-" * (total_width - 2) + "+")  # Print border line
    
    print_separator()  # Top border
    for i, row in enumerate(data):
        row_content = " | ".join(f"{item:<{col_widths[j]}}" for j, item in enumerate(row))
        print("| " + row_content + " |")  # Print row with formatting
        if i == 0:  # Print separator after header row
            print_separator()
    print_separator()  # Bottom border

# Set the path to your CSV file (change "data.csv" to your actual file path)
file_path = "data.csv"
data = read_csv(file_path)
print_table(data)