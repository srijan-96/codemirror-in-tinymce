tinymce.init({
	/*
	 * convert all the text areas with class
	 * tinymce into tinymce editors
	 */
	selector: "textarea.tinymce",
	branding: false,
	plugin: 'codemirror',
	external_plugins: {
    	codemirror: "plugins/codemirror/plugin.js"
    },
	toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | code',
	codemirror :{
		indentOnInit: true,
		path:'codemirror-5.38.0',
		config: {
			lineNumbers: true
		}
	}
});