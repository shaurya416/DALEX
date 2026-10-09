def intersect_unsorted(values, potential_values):
    """Return an unsorted intersection of two lists"""
    return [val for val in values if val in potential_values]


def convert_float_to_str(x, sign=""):
    """convert floats to str but do better than numpy and pandas"""
    if hasattr(x, 'values'):
        x = x.values
    y = [None]*len(x)
    for i, val in enumerate(x):
        y[i] = sign+str(val) if val > 0 else str(val)
    return y


def set_columns(df, columns):
    """Set `columns` on a pd.DataFrame, matching existing column names when possible

    If `df` already has exactly the names in `columns` (in any order), the columns
    are reordered by name; otherwise `columns` are assigned by position.
    """
    if df.columns.is_unique and columns.is_unique and set(df.columns) == set(columns):
        return df.loc[:, columns]
    df.columns = columns
    return df
