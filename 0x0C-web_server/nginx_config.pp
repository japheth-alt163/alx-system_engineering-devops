# Install Nginx
# With Puppet

exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

class { 'nginx':
  default_vhost => false,
}

nginx::resource::location { '/redirect_me':
  ensure   => present,
  location => '^/redirect_me',
  vhost    => 'default',
  content  => 'return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;',
  require  => Class['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
