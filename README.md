# grade_project
Import Section
•	The program starts by importing the sys module, which allows the script to read arguments from the command line.
Function: read_gradebook(file_path)
•	Opens the specified input file and reads each line.
•	Each line is expected to contain a student name and a grade, separated by a comma.
•	The line is split into two parts: the student name and the grade.
•	If the line does not contain exactly two parts, it is skipped as malformed.
•	The grade is converted to a floating-point number.
•	If the conversion fails, a message is printed and the line is skipped.
•	Successfully parsed data is stored in a dictionary called gradebook, where the key is the student name and the value is the grade.
•	If the file is not found, an error message is printed and the program exits.
•	Returns the dictionary containing all valid student data.
Function: calculate_average(gradebook)
•	Calculates the average of all grades in the gradebook dictionary.
•	Returns zero if the dictionary is empty.
•	Otherwise, it returns the sum of all grades divided by the number of students.
Function: find_min_max(gradebook)
•	Finds the minimum and maximum grades in the gradebook.
•	Identifies the students who got those minimum and maximum grades.
•	Returns two pairs of values:
o	One for the minimum grade and a list of students who received it.
o	One for the maximum grade and a list of students who received it.
Function: students_above_threshold(gradebook, threshold=70)
•	Checks which students scored above a specified threshold (default is 70).
•	Returns a list of tuples with student names and their grades if they scored above the threshold.
Function: write_report(gradebook, output_path)
•	Calculates the class average using the calculate_average function.
•	Finds the highest and lowest grades and the students who earned them.
•	Gets the list of students who scored above the threshold.
•	Writes a formatted report to the specified output file, including:
o	Class average.
o	Highest and lowest grades with corresponding student names.
o	List of students who scored above 70.
•	Prints a message confirming the report has been written.
Function: main()
•	First checks if exactly two command-line arguments are provided (input and output file paths).
•	If not, prints usage instructions and exits.
•	If valid arguments are provided:
o	Reads the gradebook data from the input file.
o	If no valid student data is found, prints an error and exits.
o	Otherwise, writes the grade summary report to the output file.
Conditional Execution: if __name__ == "__main__"
•	Ensures that the main() function only runs when this file is executed directly.
 
grade.py
•	This is the name of your Python script
D:/output/Student.txt
•	It is the input file. It should contain the student names and grades.
D:/output/gradebook_report.txt
•	It is the output file. Script writes a summary report to this file after processing the data.
D:/output/
•	It is the location of input and output file. 
Student.txt and gradebook_report.txt are the name of input and output file.

To run the Code from the terminal input: 
•	  pytohn3 grade.py student.py result_book.txt 

