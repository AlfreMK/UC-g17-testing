def foo(a=2):
    Profile.record('foo', [a])
    return a
foo(2)
foo()