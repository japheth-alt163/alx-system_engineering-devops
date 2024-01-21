# 100-puppet_ssh_config.pp

include stdlib

# Ensure the SSH client configuration file exists
file { '/etc/ssh/ssh_config':
  ensure => 'present',
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

# Turn off password authentication
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

# Declare identity file
file_line { 'Declare identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
