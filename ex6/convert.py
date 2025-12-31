def dd_to_dms(dd, is_latitude):
    direction = ""
    value = abs(dd)
    degrees = int(value)
    minutes_float = (value - degrees) * 60
    minutes = int(minutes_float)
    seconds = round((minutes_float - minutes) * 60, 2)

    if is_latitude:
        direction = "N" if dd >= 0 else "S"
    else:
        direction = "E" if dd >= 0 else "W"

    return [degrees, minutes, seconds, direction]

anchorage_dd = [-149.9002, 61.2181]
anchorage_dms = [
    dd_to_dms(anchorage_dd[0], is_latitude=False),
    dd_to_dms(anchorage_dd[1], is_latitude=True)
]

print(anchorage_dms)