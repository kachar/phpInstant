import sublime, sublime_plugin, subprocess, os, re

class phpInstantCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		# Check if Syntax is PHP else exit with message
		if self.view.settings().get('syntax') != 'Packages/PHP/PHP.tmLanguage':
			self.output('This doesn`t seem to be a valid PHP File', 'Error:')
			return False

		# Get selection, if empty get tabs complete document
		if len(self.view.substr(self.view.sel()[0])) != 0:
			selection = self.view.substr(self.view.sel()[0])
		else:
			selection = self.view.substr(sublime.Region(0, self.view.size()))
		
		code = selection
		if "<?" in code:
			part, value = code.split("<?",1)		
			if "?>" not in part:
				code = '?>' + code

		code = "eval(base64_decode('%(code)s'));" % \
		{"code": code.encode("base64").replace('\n', '')}

		# Get PHP binary path if it is set
		if self.view.settings().has('php_binary_path'):
			path = os.path.realpath(self.view.settings().get('php_binary_path')) + "/"
		else: path = ''

		# Prepare command to execute
		command = '%(path)sphp -r "%(code)s"' % \
		{"path": path, "code": code}
		
		# Execute the command
		result, e = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()
		
		# Display Result
		self.output(result, 'PHP-Result:')
		

	def single_line_output(self, title, value):
		self.view.window().show_input_panel(title, value, None, None, None)

	def multi_line_output(self, value, panel_name = 'phpInstant'):
		# Create the output Panel and start edit
		panel = self.view.window().get_output_panel(panel_name)
		edit = panel.begin_edit()

		# Insert value and end edit
		panel.insert(edit, panel.size(), value + '\n')
		panel.end_edit(edit)

		# Show the panel
		self.view.window().run_command("show_panel", {"panel": "output." + panel_name})

	def output(self, value, title = ''):
		if self.view.settings().get('phpinstant_singleline_output'):
			self.single_line_output(title, value)
		else:
			self.multi_line_output(value)

	def is_visible(self):
	    view = sublime.active_window().active_view()
	    if view:
	    	return view.settings().get('syntax') == 'Packages/PHP/PHP.tmLanguage'
