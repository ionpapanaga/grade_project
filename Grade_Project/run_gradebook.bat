@echo off
REM Batch file to run the grade.py script with input and output file paths

REM Define input and output file paths
SET INPUT_FILE=D:\data\Student.txt
SET OUTPUT_FILE=D:\data\gradebook_report.txt

REM Run the Python script with arguments
python grade.py %INPUT_FILE% %OUTPUT_FILE%

pause
