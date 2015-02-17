# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos7-updated-20150209"
  config.vm.box_url = "https://www.dropbox.com/s/ojfambfh4m40c0t/centos7-updated-20150209.box?dl=1"

  config.vm.provision :fabric do |fabric|
    fabric.fabfile_path = "./provision.py"
    fabric.tasks = ["execute"]
  end
end