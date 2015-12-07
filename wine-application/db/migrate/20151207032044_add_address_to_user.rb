class AddAddressToUser < ActiveRecord::Migration
  def change
    add_column :users, :address1, :string
    add_column :users, :address2, :string
    add_column :users, :postcode, :string
    add_column :users, :name, :string
  end
end
