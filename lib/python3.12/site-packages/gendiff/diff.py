def build_diff(data1, data2):
    keys = data1.keys() | data2.keys()
    diff = []
    for key in sorted(keys):
        if key in data1 and key not in data2:
            diff.append({
                'status': 'deleted',
                'key': key,
                'value': data1[key]
            })
        elif key in data2 and key not in data1:
            diff.append({
                'status': 'added',
                'key': key,
                'value': data2[key]
            })
        elif data1[key] == data2[key]:
            diff.append({
                'status': 'unchanged',
                'key': key,
                'value': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'status': 'parent',
                'key': key,
                'children': build_diff(data1[key], data2[key])
            })
        else:
            diff.append({
                'status': 'changed',
                'key': key,
                'value1': data1[key],
                'value2': data2[key]
            })
    return diff
