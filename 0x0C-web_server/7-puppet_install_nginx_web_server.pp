# Install NginX
# With puppet

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
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

# Add a redirect for /redirect_me
nginx::resource::location { 'redirect_me':
  location => '/redirect_me',
  ensure   => present,
  server   => 'default',
  content  => 'rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require  => Package['nginx'],
  notify   => Service['nginx'],
}
