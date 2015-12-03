class CreateWines < ActiveRecord::Migration
  def change
    create_table :wines do |t|
      t.string :name
      t.string :image
      t.text :long_description
      t.string :country
      t.string :grape
      t.boolean :vegetarian
      t.integer :size
      t.float :price
      t.text :short_description

      t.timestamps null: false
    end
  end
end
