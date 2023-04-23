#!/usr/bin/env pup
# Create ssh config file with Puppet

file_line { 'Turn off passwd auth':
  line   => '    PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
}

file_line { 'Declare identity file':
  line   => '    IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
}
