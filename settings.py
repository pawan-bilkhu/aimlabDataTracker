import os


def joinpath(*args):
    return os.path.join(*args)


# Paths to all subdirectories
ROOT = os.path.dirname(__file__)
DATA = joinpath(ROOT, 'data')
SCRIPTS = joinpath(ROOT, 'scripts')

