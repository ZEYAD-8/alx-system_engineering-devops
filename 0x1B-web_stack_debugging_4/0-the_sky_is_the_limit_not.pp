# Script to increase the number of requests Nginx web server can take
exec { 'Increase Nginx ULIMIT':
  command => 'sudo sed -i "s/15/4096/" /etc/default/nginx; sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  returns => [0, 1]
}
