import os
import requests
import pytest
import sys
import io

if len(sys.argv) != 2:
    print("Usage: python script.py <TestCaseURL>")
    sys.exit(1)

# Read the direct download link of the Dropbox file from command line arguments
dropbox_url = sys.argv[1]

# Download the test script content
response = requests.get(dropbox_url)
if response.status_code != 200:
    raise ValueError("Failed to download test script from Dropbox.")
test_script_content = response.text

# Use exec to dynamically execute the test script content
exec(test_script_content)

# Capture pytest output
stdout = io.StringIO()  # Create a StringIO object to capture standard output
stderr = io.StringIO()  # Create a StringIO object to capture standard error
sys_stdout = sys.stdout  # Save the current standard output
sys_stderr = sys.stderr  # Save the current standard error

try:
    sys.stdout = stdout  # Redirect standard output to the StringIO object
    sys.stderr = stderr  # Redirect standard error to the StringIO object
    result = pytest.main(["-v"])  # Run pytest with verbose output
finally:
    sys.stdout = sys_stdout  # Restore standard output
    sys.stderr = sys_stderr  # Restore standard error

# Print pytest results
print(stdout.getvalue())  # Print the captured standard output
print(stderr.getvalue())  # Print the captured standard error
