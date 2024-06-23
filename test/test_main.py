import sys
import os
import pytest


# Add the parent directory to sys.path to import main
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from main import main


# Use capsys to capture print output
def test_main(capsys):
    main()
    # Capture the output of main()
    captured = capsys.readouterr()
    # Check if the output matches expected
    assert captured.out == "Hello world\n"
