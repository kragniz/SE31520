# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "stereoit/fedora23-cloud"

  config.vm.provision "ansible" do |ansible|
      ansible.playbook = "provisioning/common.yml"
  end

  config.vm.define :app, primary: true do |app|
      app.vm.network "private_network", ip: "192.168.103.101"

      app.vm.provision "ansible" do |ansible|
          ansible.playbook = "provisioning/app.yml"
      end
  end

  config.vm.define :supplier do |supplier|
      supplier.vm.network "private_network", ip: "192.168.103.102"

      supplier.vm.provision "ansible" do |ansible|
          ansible.playbook = "provisioning/supplier.yml"
      end
  end

end
