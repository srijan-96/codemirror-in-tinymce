function tiny_mce_init(htmlContent) {

	tinymce.init({
		/*
		* convert all the text areas with class
		* tinymce into tinymce editors
		*/
		mode: 'textareas',
		selector: "textarea.tinymce",
		branding: false,
		force_br_newlines: true,
		force_p_newlines: false,
		forced_root_block: '',
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
		},
		setup: function (editor){
			editor.on('init', function() {
				editor.setContent(htmlContent, {format: 'raw'});
			})
		}
	});
	tinymce.render();
}