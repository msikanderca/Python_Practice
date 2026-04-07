import argparse
parser = argparse.ArgumentParser()
 parser.parse_args()
Namespace()
 parser.parse_args("-a")
usage: [-h]
: error: unrecognized arguments: - a


class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

#and it'll work the exact same way as the argparse Namespace class when it comes to attributes:

 args = Namespace(a=1, b='c')
 args.a
1
 args.b
'c'

#Alternatively, just import the class; it is available from the argparse module:

from argparse import Namespace

args = Namespace(a=1, b='c')
#As of Python 3.3, there is also types.SimpleNamespace, which essentially does the same thing:

 from types import SimpleNamespace
 args = SimpleNamespace(a=1, b='c')
args.a
1
 args.b
'c'