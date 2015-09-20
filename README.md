# Requirements
* VirtualBox (https://www.virtualbox.org/)
* Vagrant (https://www.vagrantup.com/)

## Server Architecture
* Ubuntu - Trusty Tahr 32 Bit
* Python - 2.7.6 (Ubuntu Default)
* Nginx - Latest version from Ubuntu's Source
* Uwsgi - Latest version from Pip
* PostgreSQL - Latest version from Ubuntu's Source

## Installing/Running
1. Clone this repository
2. Open the root directory in your favorite CLI
3. Run `vagrant up`
  * First run will take a while as it needs to download the VM and run provision
4. (Optional) Map 192.168.0.42 to fuel-tracker.dev in your hosts file

Load up the site in your favorite browser and enjoy!
When you're done just run `vagrant halt` to shut down the VM