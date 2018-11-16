# require 'pry'
# binding.pry

lines = File.readlines('./testcase', :chomp => true)
distances = lines.length
city_hash = {}
city_count = 0
while distances > 0
  distances -= city_count
  city_count += 1
end

city_distance = Array.new(city_count) { Array.new(city_count) { 0 } }

lines.each do |i|
  cities, distance = i.split(' = ')
  from, to = cities.split(' to ')
  if city_hash.values.max == nil
    city_hash[from] = 0
    city_hash[to] = 1
  else
    city_hash[from] = city_hash.values.max + 1 unless city_hash.key?(from)
    city_hash[to] = city_hash.values.max + 1 unless city_hash.key?(to)
  end
  city_distance[city_hash[to]][city_hash[from]] = distance.to_i
  city_distance[city_hash[from]][city_hash[to]] = distance.to_i
end
