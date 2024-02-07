# File: nginx_setup.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80;

    # Redirect /redirect_me to a new location with a 301 Moved Permanently
    location /redirect_me {
        return 301 http://\$host/;
    }

    # Return 'Hello World!' for the root path
    location / {
        return 200 'Hello World!';
    }
}
",
  notify => Service['nginx'],
}

# Remove default Nginx default site configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
  notify => Service['nginx'],
}
