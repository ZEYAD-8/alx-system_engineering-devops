# create a manifest that kills a process named killmenow
# using pkill with puppet

exec { 'kill_killmenow_process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => ['/bin', '/usr/bin'],
  user    => 'root',
}
