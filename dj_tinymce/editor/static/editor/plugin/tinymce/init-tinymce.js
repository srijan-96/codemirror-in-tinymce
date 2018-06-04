tinymce.init({
	/*
	 * convert all the text areas with class
	 * tinymce into tinymce editors
	 */
	selector: "textarea.tinymce",
	branding: false,
	plugins: 'codemirror fullpage',
	external_plugins: {
		codemirror: "plugins/codemirror/plugin.js",
		fullpage: "plugins/fullpage/plugin.js"
    },
    valid_elements: '*[*]',
	toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | code',
	codemirror :{
		indentOnInit: true,
		path:'codemirror-5.38.0',
		config: {
			lineNumbers: true
		}
	}
});