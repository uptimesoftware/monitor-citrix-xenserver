# Cisco XenServer Monitor

See http://uptimesoftware.github.io for more information.

### Tags 
 plugin   cisco   xenserver  

### Category

{ page.category }}

### Version Compatibility


  
    * Cisco XenServer Monitor 1.1 - 7.2, 7.1, 7.0, 6.0, 5.5, 5.4, 5.3, 5.2
  


### Description
This plugin uses the XenServer Management API and XAPI RRD to gather performance and health metrics for XenServer.


### Supported Monitoring Stations

7.2, 7.1, 7.0, 6.0, 5.5, 5.4, 5.3.x Windows, 5.3.x Linux/Solaris, 5.3, 5.2

### Supported Agents
None; no agent required

### Installation Notes
<ol>
<li><p>Install this plugin with the Plugin Manager</p></li>
<li><p>This plugin requires Python. Install Python if the OS of your Monitoring Station does not already have it.</p></li>
<li><p>Copy the following Python modules to your Python library directory:</p></li>
</ol>


<p>/scripts/MonitorXenServer/XenAPI.py
/scripts/MonitorXenServer/parse_rrd.py</p>

<p>The Python library path might be different depending on the OS.
On Posix, the typical path is /usr/lib/pythonX.Y where X.Y is the version number.
On Windows, the typical path is C:\Program Files\PythonX.Y.Z\Lib where X.Y.Z is the version number.</p>

<ol>
<li><p>Make certain the Python binary is in your PATH variable
i.e. executing "python" on the command line works</p></li>
<li><p>Add your XenServer as Virtual Nodes and add this monitor to your XenServer.</p></li>
</ol>



### Dependencies
<p>Python 2.7.x is required on the up.time Monitoring Station.</p>


### Input Variables
* Username - username to login to the XenServer* Password - password for the user

### Output Variables

* XenServer CPU Utilization (%)* XenServer Load Average* XenServer Memory Free (MB)* XenServer Memory Used (MB)* XenServer Memory Util (%)* Storage Repository Used (GB)* Storage Repository Free (GB)* Storage Repository Utilization (%)* Network Receive Rate (Kbps)* Network Send Rate (Kbps)

### Languages Used
* Python

