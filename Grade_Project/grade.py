import sys
def read_gradebook(file_path):
    """Reads student names and grades from a file into a dictionary."""
    gradebook = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue  # skip malformed lines
                name, grade = parts[0].strip(), parts[1].strip()
                try:
                    gradebook[name] = float(grade)
                except ValueError:
                    print(f"Skipping invalid grade for {name}.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    return gradebook

def calculate_average(gradebook):
    """Calculates average grade from the gradebook."""
    return sum(gradebook.values()) / len(gradebook) if gradebook else 0

def find_min_max(gradebook):
    """Finds students with the minimum and maximum grades."""
    if not gradebook:
        return None, None
    min_grade = min(gradebook.values())
    max_grade = max(gradebook.values())
    min_students = [name for name, grade in gradebook.items() if grade == min_grade]
    max_students = [name for name, grade in gradebook.items() if grade == max_grade]
    return (min_grade, min_students), (max_grade, max_students)

def students_above_threshold(gradebook, threshold=70):
    """Returns students who scored based on threshold score"""
    return [(name, grade) for name, grade in gradebook.items() if grade > threshold]

def write_report(gradebook, output_path):
    """Writes a summary report to an output file"""
    average = calculate_average(gradebook)
    (min_grade, min_students), (max_grade, max_students) = find_min_max(gradebook)
    above_threshold = students_above_threshold(gradebook)

    with open(output_path, 'w') as file:
        file.write(f"Class Average: {average:.2f}\n")
        file.write(f"Highest Grade: {max_grade} ({', '.join(max_students)})\n")
        file.write(f"Lowest Grade: {min_grade} ({', '.join(min_students)})\n\n")
        file.write("Students Above 70:\n")
        if above_threshold:
            for name, grade in above_threshold:
                file.write(f"- {name} ({grade})\n")
        else:
            file.write("None\n")

    print(f"Report written to {output_path}")


def main():
    #Defining the location of input and output file 
    if len(sys.argv) != 3:
        print("Usage: python grade.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    gradebook = read_gradebook(input_file)
    if not gradebook:
        print("No valid student data found.")
        sys.exit(1)

    write_report(gradebook, output_file)


if __name__ == "__main__":
    main()
