

class Foo:
    keydata = ['e', 'n']
    e = 'e'
    n = 'n'

    def has_private(self):
        return False


def construct(*args, **kw):
        pass


def generate(*args, **kw):
    return Foo()
