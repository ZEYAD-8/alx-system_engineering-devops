# Script to change OS config to login with holberton user & files w/ error
exec { 'Change OS config':
  command => 'sudo sed -i "s/4/40000/" /etc/security/limits.conf; sudo sed -i "s/5/50000/" /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin'],
  returns => [0, 1]
}
