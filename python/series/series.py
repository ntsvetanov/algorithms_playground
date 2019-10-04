def slices(series, length):
    if not series:
        raise ValueError("slice cannot be empty")

    if  length < 0:
        raise ValueError("lenght cannot be negative")
    
    if  length == 0:
        raise ValueError("lenght cannot be zero")
    
    if  len(series) < length:
        raise ValueError("slize lenght is too large")
    
    slice_list = []
    for i in range(0, len(series)):
        slice_ = series[i : i + length]
        if len(slice_) < length:
            break
        slice_list.append(slice_)

    return slice_list
