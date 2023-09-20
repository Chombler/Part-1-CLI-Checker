# This should test the command './run install'
# The command shoud install any required dependencies in user-land
# The command should exit 0 on success, and non-zero on failure

import subprocess as sp
import sys
import json

def run_install():
    try:
        result = sp.run("./run install", shell=True, check=True, stdout=sp.PIPE, stderr=sp.PIPE)

        if result.returncode == 0:
            return True, result.stdout.decode('utf-8')
        else:
            return False
    except sp.CalledProcessError as e:
        return False, result.stdout.decode('utf-8')
    except Exception as e:
        return False, str(e)

# This should test the command './run URL_FILE' where URL_FILE is the absolute location of a file
# containing a list of an ASCII-encoded newline-delimited set of URLs
# These URLs may be in the npmjs.com domain or come directly from GitHub
# This invocation should produce NDJSON output to stdout of the format:
# {"URL":"https://github.com/nullivex/nodist", "NET_SCORE":0.9, "RAMP_UP_SCORE":0.12345, "CORRECTNESS_SCORE":0.123, "BUS_FACTOR_SCORE":0.00345, "RESPONSIVE_MAINTAINER_SCORE":0.1, "LICENSE_SCORE":1}
# Each score should be in the range [0,1] where 0 is the worst and 1 is the best
# The NET_SCORE is the weighted average of the other scores, and should be be in the range [0,1]
# Each score should have up to 5 decimal places of precision, with no trailing zeroes
# The command should exit 0 on success, and non-zero on failure
def run_urlfile():
    def check_score(score):
        if 0 <= score <= 1:
            return True
        else:
            return False

    try:
        url_file = "samples.txt"
        result = sp.run('./run f{url_file}', shell=True, check=True, stdout=sp.PIPE, stderr=sp.PIPE)

        if result.returncode == 0:
            # Parse NDJSON output
            parsed_output = [json.loads(line) for line in result.stdout.strip().split('\n')]
            return True, parsed_output

            for output in parsed_output:
                check.append(
                    check_score(output['NET_SCORE']) and 
                    check_score(output['RAMP_UP_SCORE']) and 
                    check_score(output['CORRECTNESS_SCORE']) and 
                    check_score(output['BUS_FACTOR_SCORE']) and
                    check_score(output['RESPONSIVE_MAINTAINER_SCORE']) and
                    check_score(output['LICENSE_SCORE'])
                );

            if all(check):
                print("Score outupts are in the correct format.")
            else: 
                print("Score outputs are not in the correct format.")
    except sp.CalledProcessError as e:
        print(result.stdout.decode('utf-8'))
    
    except Exception as e:
        print(str(e))
    
# This should test the command './run test' where test is a test suite
# The minimum requirement for this test suite is that it conatins at least 20 distinct test cases, and 
# achieves at least 80% code coverage
# The command should output to stdout the results of the test suite in the following format:
# "X/Y test cases passed. Z% line coverage acheived."
# The command should exit 0 on success, and non-zero on failure
def run_test():
    return None

# Suggestions:
# - The success of ./run install can really only be tested indirectly by running the other commands
# - Consider bundling a copy of the sample URL_FILE we provide in this repo, then either determing its
#   absolute path at runtime, or using a relative path to it
# - Note the difference between what is outputted to stdout and what is supposed to be returned from each command
def main():
    
    #Install Test
    install_success, output =  run_install()
    if install_success:
        print('\033[92m' + "Install Sucessful" + '\033[0m');
    else:   
        print('\033[91m' + "Install Failed" + '\033[0m');
        print(output);
        sys.exit(1)
    
main()

