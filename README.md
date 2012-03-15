# phpInstant - SublimeText2 Plugin

Execute selected php-Code (or the whole document) directly from your SublimeText2 Editor and see the result

## Installation

You have three ways to install the phpInstant: using git, installing it manually or using the SublimeText2 "Package Controll" (Available here: http://wbond.net/sublime_packages/package_control)

### Install using git

To install this Plugin via git, simply browse to your 'Packages' folder like this:

for Windows
	
	cd %APPDATA%/Sublime Text 2/Packages

for OS X
	
	cd ~/Library/Application Support/Sublime Text 2/Packages

for Linux
	
	cd ~/.Sublime Text 2/Packages

for Portable Installations
	
	cd PATH_TO_PORTABLE_INSTALLATION/Sublime Text 2/Data/Packages

and clone this repository
	
	git clone https://github.com/PhilippSchaffrath/phpInstant


### Install manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to 'phpInstant'
* Copy the folder to your Sublime Text 2 'Packages' directory

### Install using Package Control

If you are familiar with Package Control you definetly know what to do, if not, go to [SublimeText2 - Package Control](http://wbond.net/sublime_packages/package_control) click on 'Install' and follow the instructions

## Settings

The following settings are available and optional, but the default settings should be mostly what you want if you install this plugin
	
	{
		"php_binary_path": "YOUR_PHP_BINARY_PATH",
		"phpinstant_singleline_output": false
	}

php_binary_path: The path to your PHP binary (fallback: "php"-call)
phpinstant_singleline_output: true for output in a single output-line (cursor jumps right in)

## Usage

The Plugin differs in two Modes:

	PHP-Mode: if the current selection, or if nothing is selected, the whole document starts with PHP-Code (this Mode is pretty accommodating, so it could even work if the selection starts with HTML or Plaintext)

	HTML-Mode: if the current selection, or if nothing is selected, the whole document starts with HTML-Code or Plaintext

If the PHP-Syntax is active, select the piece of code you want to get an output from, or select nothing, so the whole file will be used and press this shortcut:

	Ctrl+Shift+X (PHP-Mode)

If your output will contain a parse error on line 1, you should try the HTML-Mode, you have 3 ways to do this:

* Ctrl+Shift+Y (Quick Panel) and select the Mode you want to run
* Ctrl+Shift+P (Command Palette), type "phpInstant" and select the Mode you want to run
* Rightclick in the document and select the Mode you want to run from the "phpInstant"-Menu

## Release Notes

phpInstant is designed to work with the latest [development build](http://www.sublimetext.com/dev) of Sublime Text 2

## Development

I'm maybe going to add Support for other languages, but at this point it`s just available for php
