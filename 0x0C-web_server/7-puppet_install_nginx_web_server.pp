# nginx_config.pp

class { 'nginx':
  ensure  => 'installed',
  service => 'running',
  require => Package['nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
  content => '<!DOCTYPE html>
              <html>
              <head>
                  <title>Hello World!</title>
              </head>
              <body>
                  <h1>Hello World!</h1>
              </body>
              </html>',
  require => Class['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  source  => 'puppet:///modules/nginx/default',
  notify  => Service['nginx'],
  require => Class['nginx'],
}

# Create a symlink to enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Define a location block for the 301 redirect
nginx::resource::location { '/redirect_me':
  ensure   => present,
  location => '^/redirect_me',
  vhost    => 'default',
  content  => 'return 301 https://www.example.com;',
  require  => Class['nginx'],
}

