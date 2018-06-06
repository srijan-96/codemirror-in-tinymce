# Checks if the iframe is required for showing the styles
# Will check if the style tag is empty 
# if it is empty, return as it is
# otherwise wrap it in our custom iframe
template = '''<iframe id="mySpecialIframe" width="100%" height="0px" frameborder="0" style="margin: 0px !important; min-height: 5px;"></iframe>
	<script type="text/javascript">
		function writeInMyIFrame() {
			var htmlString = String.raw`$$$`;
			var myIframe = document.getElementById("mySpecialIframe").contentWindow;
			myIframe.document.open();
			myIframe.document.write(htmlString);
			myIframe.document.close();
		}
		window.addEventListener('DOMContentLoaded', function doStuff(e) {
			var myIframe = document.getElementById("mySpecialIframe");
			myIframe.addEventListener("load", function(e) {
				myIframe.height = myIframe.contentWindow.document.body.scrollHeight;
				alert(myIframe.height);
			});
			document.close();
		})
		window.onload = writeInMyIFrame;
	</script>
    '''

def process_for_iframe(htmlContent):
    ret = htmlContent
    print(template)
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
        parts = template.split('$$$')
        ret = parts[0] + htmlContent + parts[1]
    return ret