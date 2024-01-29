# SSH connection configuration
# Sets up a client SSH configuration file so we can connect without a password

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}

service { 'ssh':
  ensure  => 'running',
  enable  => true,
  require => File_line['Turn off passwd auth', 'Declare identity file'],
}
