import six
def drawstars(x):
    for i in x:
        if isinstance(i, six.string_types):
            print i[0][0].lower()
        else:
            print "*" * i

drawstars([4, 3, 'moons', 2, 'Cats'])
