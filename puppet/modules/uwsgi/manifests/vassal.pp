# == Define: vassal
#
# Adds a uwsgi vassal
#
define uwsgi::vassal(
  $socket = $name,
  $project = $name,
  $application = $name
) {

  file { "/etc/uwsgi/vassals/${name}.ini":
    content => template('uwsgi/vassal-ini.erb'),
    require => Package['uwsgi'],
    notify => Service['uwsgi']
  }
}