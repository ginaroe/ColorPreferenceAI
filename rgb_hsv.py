def rgb_to_hsv(r, g, b):
    
    r, g, b = r/255.0, g/255.0, b/255.0

    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val

    if delta == 0:
        hue = 0
    elif max_val == r:
        hue = ((g - b) / delta) % 6
    elif max_val == g:
        hue = ((b - r) / delta) + 2
    else:
        hue = ((r - g) / delta) + 4

    hue = round(hue * 60)

    if max_val == 0:
        sat = 0
    else:
        sat = delta / max_val

    val = max_val

    return (hue/360.0, sat, val)