import sublime
import sublime_plugin
import subprocess
import os
import re


class phpInstant(sublime_plugin.TextCommand):

    def interpretPHP(self, php_mode=True):
        # Check if Syntax is PHP else exit with message
        if not self.is_visible():
            return False

        # Get selection, if empty get tabs complete document
        if len(self.view.substr(self.view.sel()[0])) != 0:
            selection = self.view.substr(self.view.sel()[0])
        else:
            selection = self.view.substr(sublime.Region(0, self.view.size()))

        # Handle PHP- and HTML-modes
        code = selection
        if php_mode is True:
            #PHP-Mode close PHP-tag if an opening one is at the beginning
            if "<?" in selection:
                part, value = selection.split("<?", 1)
                if "?>" not in part:
                    code = '?>' + selection
        else:
            #HTML-Mode close PHP-tag at beginning
            code = '?>' + selection

        # base64 to prevent from bad characters
        code = "eval(base64_decode('%(code)s'));" % \
            {"code": code.encode("base64").replace('\n', '')}

        # Get PHP binary path if it is set
        if self.view.settings().has('php_binary_path'):
            path = os.path.realpath(self.view.settings().get('php_binary_path')) + "/"
        else:
            path = ''

        # Prepare command to execute
        command = '%(path)sphp -r "%(code)s"' % \
            {"path": path, "code": code}

        # Execute the command
        result, e = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()

        # Display Result
        self.output(result, 'PHP-Result:')

    def output(self, value, title=''):
        if self.view.settings().get('phpinstant_singleline_output'):
            self.single_line_output(title, value)
        else:
            self.multi_line_output(value)

    def single_line_output(self, title, value):
        self.view.window().show_input_panel(title, value, None, None, None)

    def multi_line_output(self, value, panel_name='phpInstant'):
        # Create the output Panel and start edit
        panel = self.view.window().get_output_panel(panel_name)
        panel.set_read_only(False)
        panel.set_syntax_file('Packages/Text/Plain text.tmLanguage')
        edit = panel.begin_edit()
        panel.insert(edit, panel.size(), value)
        panel.end_edit(edit)
        panel.set_read_only(True)
        self.view.window().run_command("show_panel", {"panel": "output." + panel_name})

    def is_visible(self):
        # This Plugin should just work in specific syntaxes
        view = sublime.active_window().active_view()
        if view:
            syntax = view.settings().get('syntax')
            if self.view.settings().get('phpinstant_allowed_syntax'):
                words = self.view.settings().get('phpinstant_allowed_syntax')
            else:
                words = ["php"]
            exactMatch = re.compile(r'\b%s\b' % '\\b|\\b'.join(words), flags=re.IGNORECASE)
            return exactMatch.findall(syntax)


# Command to run in PHP-Mode
class phpInstantPhpCommand(phpInstant):

    def run(self, edit):
        self.interpretPHP(True)


# Command to run in HTML-Mode
class phpInstantHtmlCommand(phpInstant):

    def run(self, edit):
        self.interpretPHP(False)


# Command to display Quick-Panel
class phpInstantQuickPanelCommand(phpInstant):

    def run(self, edit):
        if self.is_visible():
            self.view.window().show_quick_panel(['phpInstant (PHP Mode)', 'phpInstant (HTML Mode)'], self.done)

    def done(self, number):
        if number == 0:
            self.interpretPHP(True)
        elif number == 1:
            self.interpretPHP(False)
        else:
            return
