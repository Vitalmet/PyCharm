import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from capitalize import capitalize

assert capitalize("hello") == "Hello"
assert capitalize("") == ""
