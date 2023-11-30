part 4a. git hooks -- Jonathan Seibert

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

part 4b.

part 4c Activities

Created a simple logging class with a single function that returns a logger. Added some test code in the file to make sure the logger is working.
Added forensics to the following five functions
In parser.py added forensics to the following functions
checkIfWeirdYAML
checkParseError
In scanner.py added forensics to the following functions
getYAMLFiles
In graphtaint.py added forensics to the following functions
getSHFiles
In TEST_SCANNING.py added forensics to the following functions
testSecret1