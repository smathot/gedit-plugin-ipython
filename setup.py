#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
gedit-plugin-ipython
Copyright 2012 Sebastiaan Mathot <s.mathot@cogsci.nl>

This file is part of gedit-plugin-ipython.

gedit-plugin-ipython is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

gedit-plugin-ipython is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with gedit-plugin-ipython.  If not, see <http://www.gnu.org/licenses/>.
"""

import glob
from libqnotero.qnotero import Qnotero
from distutils.core import setup

setup(name='gedit-plugin-ipython',

	version = '0.10',
	description = 'Gedit plugin to run selected text in IPython',
	author = 'Sebastiaan Mathot',
	author_email = 's.mathot@cogsci.nl',
	url = 'http://www.cogsci.nl/',
	scripts = ['ipython-listener'],
	data_files=[
		('/usr/lib/gedit/plugins', ['plugin/ipython.plugin',
			'plugin/ipython.py']),
		]
	)
