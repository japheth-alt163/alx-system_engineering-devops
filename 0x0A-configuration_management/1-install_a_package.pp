# 1-install_a_package.pp

package { 'Flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
