# Automated version of QUESTION 0.

exec {'update':
	command	=> 'usr/bin/apt-get update',
	path	=> 'usr/bin:/usr/sbin:/bin',
	user	=> 'root',
}

package {'Nginx':
	ensure	=>'installed'
}

firewall {'Nginx':
	port	=> '80',
	action	=> 'Allow',
}
file {'/var/www/html':
	ensure	=> 'directory',
	owner	=> 'root',
	group	=> 'root',
	mode	=> '0755',
}

file {'/var/www/html/index.html':
	content	=> 'Hello World!\n'
}

file { 'http_header':
	path	=> '/etc/nginx/nginx.conf',
 	match	=> 'http {',
	line	=> "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
exec {'run_service':
  command => '/usr/sbin/service nginx restart',
}
