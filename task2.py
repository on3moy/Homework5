"""
Read a text file named “book.txt” that may have multiple lines. Then create a “summary.txt” file that has the frequency of each letter, case-insensitive, i.e., “a” and “A” are the same letter. Each line has a record of the letter and frequency. The last line should be a summary to tell if the file has all 26 letters. A sample “summary.txt” is:

A 25
C 36
…
X 2
Z 4

It doesn’t have all letters.

Another “book.txt” may generate the “summary.txt” as the following:

A 25
B 36
…
X 2
Y 1
Z 4

It has all letters.
"""

file_name = 'book.txt'
read_mode = 'r'

letters = []
frequency = []
try:
    with open(file_name, read_mode) as content:
        for line in content:
            content = line.rstrip('\n')
            for letter in content:
                if letter.lower() not in letters and ord(letter.lower()) >= 97 and ord(letter.lower()) <= 122:
                    letters += [letter.lower()]
                    frequency += [[letter.lower(),1]]
                else:
                    for bracket in frequency:
                        if letter.lower() in bracket[0]:
                            frequency[frequency.index(bracket)][1] += 1
    letters.sort()
    summary = 'summary.txt'
    write_mode = 'w'
    
    with open(summary,write_mode) as text:
        for letter in letters:
            for bracket in frequency:
                if letter == bracket[0]:
                    text.write(f'{bracket[0].upper()} {bracket[1]}\n')
except:
    print(f'File {file_name} not found')