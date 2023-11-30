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

I created a simple logging class with a single function that returns a logger. The logger creates a new file for that day that will contain every log that occurs on that day. The log's themselves provide a timestamp, configurable message, and a log level when used. Added some test code in the file to make sure the logger is working. Added forensics to the following methods in the TestParsing class to test the log as well as provide info:
- testKeyExtraction
- testKeyPathLength
- testKeyPath1
- testKeyPath2
- testKeyCount

While this is only for a few methods of the whole repo, it outlines how the class I made could be used to log information that could be relevant after the fact when analyzing code. In the cases above it is just to log when testing occurs, but the message could be changed to fit any section of the code. This would be useful when going back over the code when a security issue occurred. Working on this example, it made me think about where I should place code that will be used for forensics. Additionally, it made me think about what kind of information I should include in a log. Specifically, what kind of level each log should be, the code's status,  where it occurred etc. I also gained experience working with pythons logging class which I will be able to use for work I might do in the future that involves python.
