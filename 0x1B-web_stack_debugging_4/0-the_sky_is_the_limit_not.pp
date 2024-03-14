# This Puppet manifest aims to increase the capacity of an Nginx server to handle more traffic.

# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/', # Set the path for the sed command
}

# Restart Nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/', # Set the path for the Nginx restart command
}
