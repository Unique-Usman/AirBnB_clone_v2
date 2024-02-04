# install_nginx.pp

# Update package list
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
}

# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create directory structure
file { ['/data/web_static/releases/', '/data/web_static/shared/', '/data/web_static/releases/test/']:
  ensure => directory,
}

# Create a test HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Web Static',
}

# Set up symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true,
}

# Change ownership of directories
exec { 'chown-data-directory':
  command => 'chown -R ubuntu:ubuntu /data/',
}

# Update Nginx configuration
$nginx_config_content = "\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
file_line { 'hbnb_static_config':
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/besthor permanent;',
  notify => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['hbnb_static_config'],
}

