import sublime, sublime_plugin, subprocess, os

class phpInstantCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		# Check if Syntax is PHP else exit with message
		if self.view.settings().get('syntax') != 'Packages/PHP/PHP.tmLanguage':
			self.message('Error:', 'This doesn`t seem to be a valid PHP File')
			return False

		# Get selection, if empty get tabs complete document
		if len(self.view.substr(self.view.sel()[0])) != 0:
			selection = self.view.substr(self.view.sel()[0])
		else:
			selection = self.view.substr(sublime.Region(0, self.view.size()))
			# Delete PHP-Tags if using the whole document
			selection = selection.replace('<?php', '').replace('<?', '').replace('?>', '')

		code = "eval(base64_decode('%(selection)s'));" % \
		{"selection": selection.encode("base64").replace('\n', '')}

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
		self.message('PHP-Result:', result)
		

	def message(self, title, value):
		self.view.window().show_input_panel(title, value, None, None, None)

	def is_visible(self):
	    view = sublime.active_window().active_view()
	    if view:
        	return view.settings().get('syntax') == 'Packages/PHP/PHP.tmLanguage'