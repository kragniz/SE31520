# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "stereoit/fedora23-cloud"

  config.vm.provision "ansible" do |ansible|
      ansible.playbook = "provisioning/playbook.yml"
  end
end
