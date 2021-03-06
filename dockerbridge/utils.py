"""
Holds some utility methods for dockerbridge
"""
__author__ = 'mhorst@cs.uni-bremen.de'
import sys

out = sys.stdout


def sysout(msg):
    """
    Handles logging output, because pyjsonrpc hijacks stdout.
    :param msg: Message to print
    """
    out.write(str(msg) + "\n")
    out.flush()