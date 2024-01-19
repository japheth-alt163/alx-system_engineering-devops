package { 'Flask':
  ensure          => '2.1.0',
  provider        => 'pip3',
  install_options => ['--upgrade'],  # Ensure version is exactly 2.1.0
}
