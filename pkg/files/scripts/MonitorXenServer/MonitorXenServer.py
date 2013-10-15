#!/usr/bin/env python

#http://community.citrix.com/display/xs/Getting+the+Last+RRD+Datapoints
#http://wiki.xensource.com/xenwiki/XAPI_RRDs
#host CPU util http://docs.vmd.citrix.com/XenServer/6.0.0/1.0/en_gb/api/?c=host_cpu
#there's also one for SR

# Load Monitor
#http://community.citrix.com/display/xs/A+simple+load+monitor


import time
import XenAPI
import parse_rrd
import getopt
import sys, inspect


def get_host_metric(rrd_updates,metric):
	max_time=0
	data=""
	for row in range(rrd_updates.get_nrows()):
		epoch = rrd_updates.get_row_time(row)
		dv = str(rrd_updates.get_host_data(metric,row))
		if epoch > max_time:
			max_time = epoch
			data = dv	
	return float(data)

def get_vm_metric(rrd_updates,uuid,metric):
	max_time=0
	data=0.0
	for param in rrd_updates.get_vm_param_list(uuid):
		if metric in param:
			for row in range(rrd_updates.get_nrows()):
				epoch = rrd_updates.get_row_time(row)
				dv = str(rrd_updates.get_vm_data(uuid,metric,row))
				if epoch > max_time:
					max_time = epoch
					data = dv
	return float(data)

#def print_latest_host_data(rrd_updates):
#    host_uuid = rrd_updates.get_host_uuid()
#    print "**********************************************************"
#    print "Got values for Host: "+host_uuid
#    print "**********************************************************"

#    for param in rrd_updates.get_host_param_list():
#        if param != "":
#            max_time=0
#            data=""
#            for row in range(rrd_updates.get_nrows()):
#                 epoch = rrd_updates.get_row_time(row)
#                 dv = str(rrd_updates.get_host_data(param,row))
#                 if epoch > max_time:
#                     max_time = epoch
#                     data = dv
#            nt = time.strftime("%H:%M:%S", time.localtime(max_time))
#            print "%-30s             (%s , %s)" % (param, nt, data)

def get_vm_cpu_util(rrd_updates,uuid):
	count = 0
	avgCPU = 0.0
	for param in rrd_updates.get_vm_param_list(uuid):
		if (param.find("cpu") != -1):
			max_time=0
			data=""
			for row in range(rrd_updates.get_nrows()):
				epoch = rrd_updates.get_row_time(row)
				dv = str(rrd_updates.get_vm_data(uuid,param,row))
				if epoch > max_time:
					max_time = epoch
					data = dv
			count = count + 1
			avgCPU = avgCPU + float(data)
	if (count == 0):
		return 0.0
	else:
		return float(avgCPU / count)

def get_vm_vif_util(rrd_updates,uuid,txORrx):
	count = 0
	avgUtil = 0.0
	for param in rrd_updates.get_vm_param_list(uuid):
		if ((param.find("vif") != -1) and (param.find(txORrx) != -1)):
			max_time=0
			data=""
			for row in range(rrd_updates.get_nrows()):
				epoch = rrd_updates.get_row_time(row)
				dv = str(rrd_updates.get_vm_data(uuid,param,row))
				if epoch > max_time:
					max_time = epoch
					data = dv
			count = count + 1
			avgUtil = avgUtil + float(data)
	if (count == 0):
		return 0.0
	else:
		return float(avgUtil / count)

def get_vm_vbd_util(rrd_updates,uuid,readORwrite):
	count = 0
	avgUtil = 0.0
	for param in rrd_updates.get_vm_param_list(uuid):
		if ((param.find("vbd_") != -1) and (param.find(readORwrite) != -1)):
			max_time=0
			data=""
			for row in range(rrd_updates.get_nrows()):
				epoch = rrd_updates.get_row_time(row)
				dv = str(rrd_updates.get_vm_data(uuid,param,row))
				if epoch > max_time:
					max_time = epoch
					data = dv
			count = count + 1
			avgUtil = avgUtil + float(data)
	if (count == 0):
		return 0.0
	else:
		return float(avgUtil / count)
		
		
#def print_latest_vm_data(rrd_updates, uuid):
#    print "**********************************************************"
#    print "Got values for VM: "+uuid
#    print "**********************************************************"
#    for param in rrd_updates.get_vm_param_list(uuid):
#        if param != "":
#            max_time=0
#            data=""
#            for row in range(rrd_updates.get_nrows()):
#                epoch = rrd_updates.get_row_time(row)
#                dv = str(rrd_updates.get_vm_data(uuid,param,row))
#                if epoch > max_time:
#                    max_time = epoch
#                    data = dv
#            nt = time.strftime("%H:%M:%S", time.localtime(max_time))
#            print "%-30s             (%s , %s)" % (param, nt, data)

#def build_vm_graph_data(rrd_updates, vm_uuid, param):
#    time_now = int(time.time())
#    for param_name in rrd_updates.get_vm_param_list(vm_uuid):
#        if param_name == param:
#            data = "#%s  Seconds Ago" % param
#            for row in range(rrd_updates.get_nrows()):                
#                epoch = rrd_updates.get_row_time(row)
#                data = str(rrd_updates.get_vm_data(vm_uuid, param_name, row))
#                data += "\n%-14s %s" % (data, time_now - epoch)
#            return data

#def format_list_of_floats(lof):
#	return "["+", ".join(["%.2f" % x for x in lof])+"]"
			
def print_usage():
	print ""
	print "Usage: "+inspect.getfile(inspect.currentframe())+" -h <host> -u <username> -p <password>"
	print "e.g. "+inspect.getfile(inspect.currentframe())+" -h 10.1.1.40 -u xenUser -p xenPassword"
	sys.exit(1)
	

def main():
	
	options, args = getopt.getopt(sys.argv[1:], 'h:u:p:','')
	for opt, arg in options:
		if opt in ('-h'):
			if arg == "":
				print_usage()
			else:
				url = "http://"+arg
		elif opt in ('-u'):
			if arg == "":
				print_usage()
			else: 
				username = arg
		elif opt in ('-p'):
			if arg == "":
				print_usage()
			else: 
				password = arg

	
			
	#url = "http://10.1.40.62"
	try:
		session = XenAPI.Session(url)
		session.xenapi.login_with_password(username,password)
	except XenAPI.Failure, e:
		if e.details[0]=='HOST_IS_SLAVE':
			print "Host is a Slave.  Add monitor to the Master to get metrics."
			sys.exit(0)
		else:
			print e.details[0]
			sys.exit(2)
	
	rrd_updates = parse_rrd.RRDUpdates()
	params = {}
	params['cf'] = "AVERAGE"
	params['start'] = int(time.time()) - 10
	params['interval'] = 5
	params['host'] = ""
	rrd_updates.refresh(session.handle, params, url)


#	for uuid in rrd_updates.get_vm_list():
#		print_latest_vm_data(rrd_updates, uuid)
#		param = 'cpu0'
#		data = build_vm_graph_data(rrd_updates, uuid, param)
#		fh = open("%s-%s.dat" % (uuid, param), 'w')
#		fh.write(data)
#		fh.close()

	# Host CPU
	for host in session.xenapi.host.get_all():
		cpu_sum = 0.0
		count = 0.0
		for cpu in session.xenapi.host.get_host_CPUs(host):			
			cpu_sum = cpu_sum + session.xenapi.host_cpu.get_utilisation(cpu)
			count = count + 1	
		avgCPU = cpu_sum / count		
		print "hostAvgCPUUtil %f" % avgCPU		
		
	# in megabyte (MB)
	memUsed = get_host_metric(rrd_updates, "memory_total_kib") / 1024
	memFree = get_host_metric(rrd_updates, "memory_free_kib") / 1024
	print "hostMemFree %f" % memFree
	print "hostMemUsed %f" % float(memUsed-memFree)
	print "hostMemPct %f" % float((memUsed - memFree)/ memUsed * 100)
	print "loadAvg %f" % float(get_host_metric(rrd_updates, "loadavg"))
	
	# Storage Repository
	for sr in session.xenapi.SR.get_all():
		srName = session.xenapi.SR.get_name_label(sr).replace(" ", "_")
		diskTotal = float( int(session.xenapi.SR.get_physical_size(sr)) / 1024 / 1024 / 1024 )
		if (diskTotal > 0 and srName.find("DVD_") == -1):
			diskUtil = float( int(session.xenapi.SR.get_physical_utilisation(sr)) / 1024 / 1024 / 1024)
			# Disk Used in GB
			print "%s.diskUsed %f" % (srName, diskUtil)
			print "%s.diskFree %f" % (srName, diskTotal-diskUtil)
			print "%s.diskUtilPct %f" % (srName, float(diskUtil/diskTotal)*100)


	for pif in session.xenapi.PIF.get_all():
		interfaceName=session.xenapi.PIF.get_device(pif)
		# Network I/O, raw data in Byte/s, convert to Kilobyte/s
		print "%s.hostNetIn %f" % (interfaceName, get_host_metric(rrd_updates, "pif_"+interfaceName+"_rx")/1000)
		print "%s.hostNetOut %f" % (interfaceName, get_host_metric(rrd_updates, "pif_"+interfaceName+"_tx")/1000)
		


		
#	# VM's 
#	# Not used because these metrics can already be acquired by up.time
#	for vm in session.xenapi.VM.get_all():
#		if not session.xenapi.VM.get_is_a_template(vm):
#			#print "%s" % session.xenapi.VM.get_name_label(vm)
#			
#			vmName=session.xenapi.VM.get_name_label(vm).replace(" ", "_")
#						
#			if session.xenapi.VM.get_power_state(vm) != "Running":
#				print "%s not running  -  %s" % (vmName, session.xenapi.VM.get_uuid(vm))
#	
#			else:
#				# CPU
#				print "%s is running  -  %s" % (vmName, session.xenapi.VM.get_uuid(vm))
#				print "%s.cpu %f" % (vmName,get_vm_cpu_util(rrd_updates,session.xenapi.VM.get_uuid(vm)))
#				
#				# Memory
#				# If XenServer Tool is not installed in the VM, we can't get the memory utilization
#				vmMemFree=get_vm_metric(rrd_updates,session.xenapi.VM.get_uuid(vm),"memory_internal_free") / 1024
#				if vmMemFree == 0:
#					vmMemTotal=0
#					print "%s.vmMemUsed %f " % (vmName,0.0) 
#					print "%s.vmMemUsedPct %f " % (vmName,0.0)
#				else:
#					vmMemTotal=get_vm_metric(rrd_updates,session.xenapi.VM.get_uuid(vm),"memory") / 1024 / 1024
#					print "%s.vmMemUsed %f " % (vmName,(vmMemTotal - vmMemFree) ) 
#					print "%s.vmMemUsedPct %f " % (vmName,(vmMemTotal - vmMemFree) / vmMemTotal * 100)
#				
#				# Network I/O, raw data in Byte/s, convert to Kilobyte/s
#				vmNetOut=get_vm_vif_util(rrd_updates,session.xenapi.VM.get_uuid(vm),"tx") / 1000
#				vmNetIn=get_vm_vif_util(rrd_updates,session.xenapi.VM.get_uuid(vm),"rx") / 1000
#				print "%s.vmNetOut %f" % (vmName,vmNetOut)
#				print "%s.vmNetIn %f" % (vmName,vmNetIn)
#				
#				# Disk I/O, raw data in Byte/s, convert to Kilobyte/s
#				vmDiskRead=get_vm_vbd_util(rrd_updates,session.xenapi.VM.get_uuid(vm),"read") / 1000
#				vmDiskWrite=get_vm_vbd_util(rrd_updates,session.xenapi.VM.get_uuid(vm),"write") / 1000
#				print "%s.vmDiskRead %f" % (vmName,vmDiskRead)
#				print "%s.vmDiskWrite %f" % (vmName,vmDiskWrite)
				
				

	session.logout()

main()