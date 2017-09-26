import re

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')
to_camel_re = re.compile(r'(?!^)_([a-zA-Z])')


def camel_to_snake(s):
    s1 = first_cap_re.sub(r'\1_\2', s)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def snake_to_camel(s):
    return to_camel_re.sub(lambda m: m.group(1).upper(), s)
