This plugin uses the XenServer Management API and XAPI RRD to gather performance and health metrics for XenServer.  


Installation Instructions
=========================
1. Install this plugin with the Plugin Manager (http://support.uptimesoftware.com/the-grid/)

2. This plugin requires Python.  Install Python if the OS of your Monitoring Station does not already have it.

3. Copy the following Python modules to your Python library directory:

	<up.time core>/scripts/MonitorXenServer/XenAPI.py
	<up.time core>/scripts/MonitorXenServer/parse_rrd.py

   The Python library path might be different depending on the OS. 
   On Posix, the typical path is /usr/lib/pythonX.Y  where X.Y is the version number.
   On Windows, the typical path is C:\Program Files\PythonX.Y.Z\Lib  where X.Y.Z is the version number.

4. Make certain the Python binary is in your PATH variable
   i.e. executing "python" on the command line works


Configuration
=============
The XenServer being monitored needs to be added to up.time as a "Virtual Node".  After that, the plugin can be added to the XenServer.


Input Variable
==============
Username - username to login to the XenServer
Password - password for the user


Output Variables
================
XenServer CPU Utilization (%)
XenServer Load Average
XenServer Memory Free (MB)
XenServer Memory Used (MB)
XenServer Memory Util (%)
Storage Repository Used (GB)
Storage Repository Free (GB)
Storage Repository Utilization (%)
Network Receive Rate (Kbps)
Network Send Rate (Kbps)
