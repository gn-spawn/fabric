# -*- coding: utf-8 -*-

from fabric.api import run, sudo, cd
from fabric.contrib.files import sed, append, contains

def execute():
    update()
    rbenv_install()
    ruby_and_rails_install()
    all_port_open()
    imagemagick()
    sqlite()
    mariadb()
    mysql_decure()
    python3()
    print u'おわりました(`>ω<\')'

def update():
    sudo('yum update -y')
    sudo('yum install -y git gcc openssl-devel libyaml-devel libffi-devel readline-devel zlib-devel gdbm-devel ncurses-devel')

def rbenv_install():
    run('git clone https://github.com/sstephenson/rbenv /home/vagrant/.rbenv')
    run('git clone https://github.com/sstephenson/ruby-build /home/vagrant/.rbenv/plugins/ruby-build')
    run('echo \'export PATH="$HOME/.rbenv/bin:$PATH"\' >> /home/vagrant/.bash_profile')
    run('echo \'eval "$(rbenv init -)"\' >> /home/vagrant/.bash_profile')

def ruby_and_rails_install():
    run('rbenv install 2.2.0')
    run('rbenv global 2.2.0')
    run('gem install rails bundler --no-ri --no-rdoc')

def all_port_open():
    sudo('firewall-cmd --set-default-zone=trusted')

def imagemagick():
    sudo('yum install -y ImageMagick-devel')

def sqlite():
    sudo('yum install -y sqlite-devel')

def mariadb():
    sudo('yum install -y mariadb mariadb-server mariadb-devel')
    sudo('systemctl enable mariadb')
    sudo('systemctl start mariadb')

def mysql_secure():
    sudo('mysql -uroot -e "UPDATE mysql.user SET Password=PASSWORD(\'root\') WHERE User=\'root\'; DELETE FROM mysql.user WHERE User=\'\'; DELETE FROM mysql.user WHERE User=\'root\' AND Host NOT IN (\'localhost\', \'127.0.0.1\', \'::1\'); FLUSH PRIVILEGES; "')


def python3():
    run('wget https://www.python.org/ftp/python/3.4.0/Python-3.4.0.tgz')
    run('tar xzvf Python-3.4.0.tgz')
    with cd('Python-3.4.0'):
        run('./configure --enable-shared --with-threads')
        run('make')
        sudo('make install')
        sudo('cp -p libpython3.4m.so libpython3.4m.so.1.0 /usr/lib')
        sudo('/sbin/ldconfig')
        run('source ~/.bash_profile')
        run('python3 --version')