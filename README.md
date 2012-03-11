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

phpInstant uses the php binary, by default it uses "php" without a binary-path. This should work fine if you have added your php binary path to your system path (you can check this if you type "php" in an terminal)

If it says the file does not exist, simply open your Sublime- "Settings - User" File and insert this setting
	
	{
		"php_binary_path": "YOUR_PHP_BINARY_PATH"
	}

## Usage

If the PHP-Syntax is active, select the piece of code you want to test, or select nothing so the whole file will be used and press this shortcut:

	Ctrl+Shift+E

or rightclick in the document and select "Instant PHP"

## Release Notes

phpInstant is designed to work with the latest [development build](http://www.sublimetext.com/dev) of Sublime Text 2

## Development

I'm maybe going to add Support for other languages, but at this point it`s just available for php
