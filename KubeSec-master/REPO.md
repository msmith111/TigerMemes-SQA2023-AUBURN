### Part 4a. git hooks - Jonathan Seibert

The task of this assignment was to create Create a Git Hook that will run and report all
security weaknesses in the project in a CSV file whenever a Python file is changed and committed. By using the
hooks directory in the .git folder, we can create a pre-commit hook from the provided pre-commit.sample file that runs
before every commit. The file was modified to use the line bandit -r -f "csv" -o "capturedSecurityWeaknesses.csv"
so that way all the bandit security weaknesses could be output when the script runs to the
capturedSecurityWeaknesses.csv file. To use this feature, you can clone the repository, copy the pre-commit file
to the .git/hooks directory, and make a commit or you can run it manually by going into the pre-commit file itself and
run the script manually to just get the output file. I learned how to use bash scripts to automatically run bandit in
a repo to report security vulnerabilities and tie it into the project to run when commits are made.
This is a useful tool because it can warn a developer about their latest code changes before merging to master.

### Part 4b. Fuzzing - Shafqat Rana

### Part 4c Forensics - Mark Smith

Created a simple logging class with a single function that returns a logger. Added some test code in the file to make sure the logger is working. Added forensics to the following methods in the TestParsing class:
- testKeyExtraction
- testKeyPathLength
- testKeyPath1
- testKeyPath2
- testKeyCount

While this only for a few methods of the whole repo, it outlines how the class I made could be used to log information that could be relevant after the fact when analyzing code. The class logs a timestamp as well as a message. In the cases above it is just to log when testing occurs, but the message could be changed to fit the section of code. Additonally, the class allows for logging a certain log type such as info or warning. 