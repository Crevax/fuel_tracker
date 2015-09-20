# create a new run stage to ensure certain modules are included first
stage { 'pre':
  before => Stage['main']
}

# add the baseconfig module to the new 'pre' run stage
class { 'baseconfig':
  stage => 'pre'
}

include baseconfig, users, nginx, postgresql, python, uwsgi

# Note: PostgreSQL doesn't like hyphens
postgresql::create-role {'fuel_admin':
}

postgresql::create-db {'fuel_tracker':
  owner => 'fuel_admin'
}

exec { 'pip installs':
  path => ["/usr/bin/","/usr/sbin/","/bin"],
  command => 'pip install -r requirements.txt',
  cwd => '/srv/www/fuel-tracker'
}

exec { 'django syncdb':
  path => ["/usr/bin/","/usr/sbin/","/bin"],
  command => 'python manage.py syncdb --noinput',
  cwd => '/srv/www/fuel-tracker',
  require => Exec['pip installs']
}

exec { 'django migrate':
  path => ["/usr/bin/","/usr/sbin/","/bin"],
  command => 'python manage.py migrate fuel_tracker',
  cwd => '/srv/www/fuel-tracker',
  require => Exec['django syncdb']
}

exec { 'django static files':
  path => ["/usr/bin/","/usr/sbin/","/bin"],
  command => 'python manage.py collectstatic --noinput',
  cwd => '/srv/www/fuel-tracker',
  require => Exec['pip installs']
}

uwsgi::vassal {'fuel-tracker':
  application => 'vehicle_archives'
}

nginx::load-server {'fuel-tracker':
  socket => 'fuel-tracker'
}