import scanner
import graphtaint

def fuzzFunctions() :

    exceptions = []

    try : scanner.getYAMLFiles(1)
    except Exception as ex: exceptions.append("Method: scanner.getYAMLFiles\nError: " + str(ex))

    try : scanner.scanForUnconfinedSeccomp('')
    except Exception as ex: exceptions.append("Method: scanner.scanForUnconfinedSeccomp\nError: " + str(ex))

    try: scanner.getItemFromSecret(0, 0)
    except Exception as ex: exceptions.append('Method: scanner.scanForSecrets\nError: ' + str(ex))

    try: graphtaint.constructHelmString({})
    except Exception as ex: exceptions.append('Method: graphtaint.constructHelmString\nError: ' + str(ex))

    try : graphtaint.mineNetPolGraph(None, None, None, None)
    except Exception as ex: exceptions.append("Method: graphtaint.mineNetPolGraph\nError: " + str(ex))

    return exceptions

if __name__ == '__main__': 

    exceptionsList = fuzzFunctions()

    for i in exceptionsList :
        print('\n' + i)