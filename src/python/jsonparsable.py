# JsonParsable adapted from http://www.seanjohnsen.com/2016/11/23/pydeserialization.html
import util.stringconvert as str_conv


class Printable:
    """ A simple class base that implements a rudimentary repr function
    """
    def __repr__(self):
        from pprint import pformat
        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=2, width=80)


class JsonParsable(Printable):
    _fields = []

    def _init_arg(self, expected_type, value):
        if isinstance(value, expected_type):
            return value
        else:
            return expected_type(**value)

    def __init__(self, **kwargs):
        # Check that _fields is properly set
        field_names, field_types = zip(*self._fields)
        assert([isinstance(name, str) for name in field_names])
        assert([isinstance(type_, type) for type_ in field_types])

        # Parse dictionary, converting camelCase json keys to snake_case fields
        for name, field_type in self._fields:
            setattr(self, name, self._init_arg(field_type, kwargs.pop(str_conv.snake_to_camel(name))))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
