#!usr/bin/pup
#Package or app installation

package { 'flask':
	require	 => '2.1.0',
	ensure	 => 'installed',
	provider => 'pip3',
}
