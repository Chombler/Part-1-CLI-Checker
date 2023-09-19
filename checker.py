# This should test the command './run install'
# The command shoud install any required dependencies in user-land
# The command should exit 0 on success, and non-zero on failure
def run_install():
    return None

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
    return None

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
    return None
