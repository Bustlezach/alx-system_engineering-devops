#!usr/bin/pup
# Execute the process kill command using pkill command

exec { 'kill':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
}

