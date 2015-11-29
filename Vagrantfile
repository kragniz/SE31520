# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "stereoit/fedora23-cloud"

  config.vm.network "private_network", ip: "10.0.0.10"

  config.vm.provision "ansible" do |ansible|
      ansible.playbook = "provisioning/playbook.yml"
  end
end
