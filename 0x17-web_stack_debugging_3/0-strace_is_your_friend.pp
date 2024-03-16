# A puppet script to fix php settings file by replacing typos

exec { 'fix_typo':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin']
}
