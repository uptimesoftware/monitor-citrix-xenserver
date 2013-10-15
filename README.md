# Composite (Aggregate) Monitor (uptime 5.x)
## Tags : plugin   aggregate   deprecated  

## Category: plugin

##Version Compatibility<br/>Module Name</th><th>up.time Monitoring Station Version</th>


  
    * Composite (Aggregate) Monitor (uptime 5.x) 1.1 - 5.5, 5.4, 5.3, 5.2
  


### Description: Check the status of other monitors to determine the aggregated state of an application (or component).
Example: trigger an alert or outage if more than 3 HTTP monitors are down (in a WARN/CRIT state) in a web cluster.
Note: This functionality is now built in up.time 6+! Just add a new Application (in My Infrastructure) to aggregate multiple monitors.

### Supported Monitoring Stations: 5.5, 5.4, 5.3, 5.2
### Supported Agents: None; no agent required
### Installation Notes: <ol>
<li>Place jar file(s) in "(uptime_dir)/core" directory</li>
</ol>


<p>If on Linux/Solaris (extra step):
- edit the /uptime.lax file and add the new jar files to the line that starts with:
lax.class.path=...</p>

<p>Note: It will be a single long line even though it looks like it's on multiple lines. Make sure the new jar filenames are on the same line.</p>

<ol>
<li><p>Restart the up.time Data Collector (core) to load the monitor into memory.</p></li>
<li><p>Place the xml file(s) in the uptime directory and run the following command(s) from the uptime directory:</p>

<blockquote><p>scripts\erdcloader -x</p></blockquote></li>
</ol>


### Dependencies: <p>n/a</p>

### Input Variables: * Service monitor name(s)* Hostname(s)
### Output Variables: * Monitors in OK State* Monitors in WARN State* Monitors in CRIT State
### Languages Used: * Java

