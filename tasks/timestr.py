__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    days = seconds // 86400
    hours = (seconds // 3600) % 24
    minutes = (seconds // 60) % 60
    remaining_seconds = seconds % 60

    # Format the time representation
    time_str = '{:02d}d'.format(days) if days else ''
    time_str += '{:02d}h'.format(hours) if hours or days else ''
    time_str += '{:02d}m'.format(minutes) if minutes or days or hours else ''
    time_str += '{:02d}s'.format(remaining_seconds)

    return time_str
