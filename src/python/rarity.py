from jsonparsable import JsonParsable


class Rarity(JsonParsable):
    _fields = [
        ('cost', int),
        ('max_level', int),
        ('max_level_growth', int),
        ('max_level_stat_multiplier_denominator', int),
        ('max_level_stat_multiplier_numerator', int),
        ('stat_combinations', dict)]
