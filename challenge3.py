def series_resistance(lst):
    return f"{total_resistance:.1f} {units}"
lst=[1, 5, 6, 3]
total_resistance = sum(lst)
units = "ohm" if total_resistance <= 1 else "ohms"
print(total_resistance)