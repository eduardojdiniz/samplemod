# -*- coding: utf-8 -*-

# context.py provide runtime context for importing the module "sample"
import sys
import os

# Because python checks in the directories in sequenctial order, starting at
# the first directory in sys.path list, till it find the .py file it is looking
# for, it may inadvertly import a module instead of a package with the same
# name. For instance:
# - test
#    - shared
#       - __init__.py
#       - phtest.py
#    - testmain.py
#    - shared.py
# the interpreter will raise an error if I try from shared import phtest from
# testmain.py: ImportError : cannot import name 'phtest'. This happens because
# it first search in the current directory and tries to get 'phtest' from
# shared.py instead of getting the module phtest inside ./shared.py
# To correct that we are going to put in sys.path at position '0' (first
# directory it will search for) the path to our module package to give the test
# package proper import context
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Then, withing the individual test modules, import the module like so:
# from context import sample. By doing this, whomever is importing this module
# with get sample in their namespace. If I were to run just import context, I
# would have to use context.sample to acess the module 'sample'
# This works because python runs modules as it get imported. It just do not
# execute code below "if __name__ == "__main__"
import sample
