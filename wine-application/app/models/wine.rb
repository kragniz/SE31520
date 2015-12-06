class Wine < ActiveRecord::Base
    def self.search(search)
        wildcard = "%#{search}%"
        where("name LIKE ? OR short_description LIKE ? OR long_description LIKE ?",
              wildcard, wildcard, wildcard)
    end
end
