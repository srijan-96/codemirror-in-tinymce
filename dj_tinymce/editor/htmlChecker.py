# Checks if the iframe is required for showing the styles
# Will check if the style tag is empty 
# if it is empty, return as it is
# otherwise wrap it in our custom iframe

def process_for_iframe(htmlContent):
    ret = htmlContent
    try:
        start = ret.index("<head>") + len("<head>")
        end = ret.index("</head>") + len("</head>")
        check = ret[start:end]
    except ValueError:
        return ret
    # Remove all whitespaces, newlines and tabs 
    check = ''.join(check.split())
    if(check == ''):
        print("You don't need an iframe")
    else:
        print("You need an iframe")
    return ret