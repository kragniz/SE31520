# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "stereoit/fedora23-cloud"

  config.vm.provision "ansible" do |ansible|
      ansible.playbook = "provisioning/playbook.yml"
  end

  config.vm.define :app do |app|
      app.vm.network "private_network", ip: "192.168.100.101"
  end

  config.vm.define :suppilier do |suppilier|
      suppilier.vm.network "private_network", ip: "192.168.100.102"
  end

end
