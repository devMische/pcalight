def replace_last(source_string, replace_what, replace_with):
    if source_string.endswith(replace_what):
        return source_string[:-len(replace_what)] + replace_with
    return source_string

# cleanstring


def cleanstr(s):
    s = s.strip()
    s = s.replace('ä', 'ae')
    s = s.replace('ö', 'oe')
    s = s.replace('ü', 'ue')
    s = s.replace('Ä', 'Ae')
    s = s.replace('Ö', 'Oe')
    s = s.replace('Ü', 'Ue')
    s = s.replace('ß', 'ss')
    s = s.replace(' ', '_')

    return s


def remove_pca_naming(s):
    s = replace_last(s, '_HANDLE', '')
    s = replace_last(s, '_EMPTY', '')
    s = replace_last(s, '_CAM', '')
    s = replace_last(s, '_DEPTH', '')
    s = replace_last(s, '_TOUR', '')
    return s
