# require 'pry'
# binding.pry

lines = File.readlines('./input', :chomp => true)
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

shortest = Float::INFINITY
longest = 0
city_hash.keys.permutation.each do |perm|
  this_distance = 0
  (0..perm.length-2).each do |i|
    this_distance += city_distance[city_hash[perm[i]]][city_hash[perm[i+1]]]
  end
  shortest = [shortest, this_distance].min
  longest = [longest, this_distance].max
end

puts "shortest = #{shortest}", "longest = #{longest}"
