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

import socket
from gi.repository import GObject, Gedit, Gtk

ui_str = """<ui>
  <menubar name="MenuBar">
    <menu name="ToolsMenu" action="Tools">
      <placeholder name="ToolsOps_2">
        <menuitem name="IPython" action="IPython"/>
      </placeholder>
    </menu>
  </menubar>
</ui>
"""

class IPythonPlugin(GObject.Object, Gedit.WindowActivatable):

	"""A Gedit plugin that sends code to a custom IPython console"""

	__gtype_name__ = "IPythonPlugin"

	window = GObject.property(type=Gedit.Window)

	def __init__(self):
	
		"""Constructor"""
	
		GObject.Object.__init__(self)		
		self.listener_port = 50007
		self.listener_host = 'localhost'
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def do_activate(self):
	
		"""Add a menu entry when the plugin is activated"""
	
		manager = self.window.get_ui_manager()
		self._action_group = Gtk.ActionGroup('IPythonPluginActions')
		self._action_group.add_actions([('IPython', None,
			_('Run in IPython'), '<Control>r', _('Clear the document'),
			self.send_to_ipython)])
		manager.insert_action_group(self._action_group, -1)
		self._ui_id = manager.add_ui_from_string(ui_str)
		
	def do_deactivate(self):
	
		"""Remove the menu entry when the plugin is deactivated"""
	
		manager = self.window.get_ui_manager()
		manager.remove_ui(self._ui_id)
		manager.remove_action_group(self._action_group)
		manager.ensure_update()

	def do_update_state(self):
	
		"""Do nothing on updates"""
	
		pass
				
	def send_to_ipython(self, action=None):
	
		"""
		Send the selected text to the IPython listener.
		
		Keyword argument:
		action -- dummy argument (default=None)
		"""
	
		doc = self.window.get_active_document()
		if doc.get_has_selection():
			start, end = doc.get_selection_bounds()			
		else:
			start, end = doc.get_bounds()
		code = start.get_text(end)
		self.socket.sendto(code, (self.listener_host, self.listener_port) )
		
