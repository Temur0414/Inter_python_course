try:
    a = 5 / 1

except Exception as e:
    print(e)


class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')


test_value(452)
