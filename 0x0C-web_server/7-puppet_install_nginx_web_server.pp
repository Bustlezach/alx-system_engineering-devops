#!/usr/bin/env pup
# This script installs Nginx through puppet

exec {'install':
	command		=> 'sudo apt-get update; sudo apt-get upgrade',
	provider 	=> 'shell',
}

package {'Nginx':
	ensure		=> 'installed'
}

exec {'Greetings':
	command		=> 'echo "Hello World" > /var/www/html/index.html',
	provider	=> 'shell',
}

exec {'listen_on_port_80':
	command		=> 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/google.com\/;\\n\\t}/" /etc/nginx/sites-available/default',
	provider	=> shell,
}

exec {'restart':
	command		=> 'service Nginx restart',
	provider	=> 'shell',
}
