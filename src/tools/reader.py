# read the whole file, return lines
def readfile(rootdir, filepath):
    lines = []
    fullfilepath = rootdir + '/' + filepath
    print(fullfilepath)
    with open(fullfilepath) as file:
        for l in file:
            if not l.startswith('#'):  # Ignore comments
                lines.append(l)
    return lines
