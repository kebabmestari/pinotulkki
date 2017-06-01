def convert_token(token):
    if token.isdigit():
        token = int(token)
    else:
        token = str(token)
        if token == 'true' or token == 'false':
            # Boolean value
            if token == 'true':
                token = True
            elif token == 'false':
                token = False
        else:
            # String value
            token = str(token)
    return token