# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
#


Wine.create(name: 'Z Test Wine',
                       image:'http://example.com/3434.jpg',
                       long_description: 'A longish description',
                       country: 'England',
                       grape: 'Big grape',
                       vegetarian: false,
                       size: 70,
                       price: 15.50,
                       short_description: 'Nice wine'
                      )

Wine.create(name: 'A Test Wine',
                       image:'http://example.com/3434.jpg',
                       long_description: 'A longish description',
                       country: 'England',
                       grape: 'Big grape',
                       vegetarian: false,
                       size: 70,
                       price: 15.50,
                       short_description: 'Nice wine'
                      )

for i in 0..20
    Wine.create(name: 'Test Wine',
                           image:'http://example.com/3434.jpg',
                           long_description: 'A longish description',
                           country: 'England',
                           grape: 'Big grape',
                           vegetarian: false,
                           size: 70,
                           price: 15.50,
                           short_description: 'Nice wine'
                          )
end
