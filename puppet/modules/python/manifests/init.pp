# == Class: python
#
# Installs python dev packages
#
class python {
  include python::packages

  package { 'python':
    ensure => installed;
  }
}
class python::packages {
  $apt = ['python-dev', 'build-essential', 'python-pip']

  package { $apt:
    require => Class['python'],
    ensure 	=> installed;
  }
}