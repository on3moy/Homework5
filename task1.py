"""
Assume that a file containing a series of student scores is named “scores.txt”.  It may have the following content:

Alice 69
Bob  89
Cindy 79


Write a program that calculates the number of students and the average of all the scores stored in the file and print the output: 

The class average is 79 for 3 students.

Also write the output to a log.txt file. You should use the with

It should handle IOError exceptions that are raised when it fails to open the file, display an error message with the detail error exception and stop. For example, it happens when there is no scores.txt in the current folder.

For the following content, it should handle any ValueError exceptions that are raised when the items
that are read from the score field are failed to be converted to a number by printing an error message and skip the record.  There could be multiple error values to be ignored. For example, the data could be:

Alice 69
Bob eight-seven
Cindy 79
David 89
Eric abc

For the above data, it should skip both Bob and Eric and display:

Bad score value for Boy, ignored.
Bad score value for Eric, ignored.
The class average is 79 for 3 students.

The log.txt file should have the same content as the above output.
"""
# Imports
import os

# Global Variables
student_scores = 'scores.txt'
read_mode = 'r'

# Lists populates if text file has relevant information
names = []
bad_names = []
scores = []

# Check if file is in directory
if os.path.isfile(student_scores):
    with open(student_scores, read_mode) as text:
        for line in text:
            # Remove extra spaces from \n
            content = line.rstrip('\n')
            name, score = content.split()
            # Check if score is  digit
            if score.isdigit():
                names += [name]
                scores += [int(score)]
            else:
                # Accumulate a list of bad names
                bad_names += [name]

    # Create a Log text file to record bad values and show class average
    with open('log.txt', 'w') as text:
        for bad_name in bad_names:
            print(f'Bad score value for {bad_name}, ignored.')
            text.write(f'Bad score value for {bad_name}, ignored.\n')
        text.write(f'The class average is {sum(scores)/len(scores)} for {len(names)} students')
    print(f'The class average is {sum(scores)/len(scores):.0f} for {len(names)} students')
else:
    try:
        open(student_scores,read_mode)
    except FileNotFoundError as error:
        print(error)
        print(f'{student_scores} is not found in Path:\n--> {os.getcwd()}\n')