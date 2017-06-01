from common import constants


# read the whole file, return lines
def readfile(rootdir, filepath):
    lines = []
    fullfilepath = rootdir + '/' + filepath
    print(fullfilepath)
    with open(fullfilepath) as file:
        for l in file:
            l = l.strip()  # strip whitespace
            if not l.startswith(constants.COMMENT_SYMBOL) and not len(l) == 0:  # Ignore comments and empty lines
                lines.append(l)
    return lines
