#!usr/bin/pup
# Execute the process kill command using pkill command

exec {'killmenow':
	command	=> 'pkill',
	path	=> '/usr/bin:/usr/sbin:/bin'
}
