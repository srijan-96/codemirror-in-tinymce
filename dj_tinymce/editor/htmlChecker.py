# Checks if the iframe is required for showing the styles
# Will check if the style tag is empty 
# if it is empty, return as it is
# otherwise wrap it in our custom iframe

def process_for_iframe(htmlContent):
    ret = htmlContent
    return ret