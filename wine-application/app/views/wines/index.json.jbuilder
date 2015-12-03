json.array!(@wines) do |wine|
  json.extract! wine, :id, :name, :image, :long_description, :country, :grape, :vegetarian, :size, :price, :short_description
  json.url wine_url(wine, format: :json)
end
