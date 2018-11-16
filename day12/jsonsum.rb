require 'json'

str = File.readlines('./input', :chomp => true)[0]

jsonary = JSON.parse(str).to_a.flatten  #turn json into hash, then convert to a flattened array
while jsonary.any? { |x| x.class == Hash } #keep looping through turning sub-hashes into flattened arrays until there's no more hashes left
  jsonary.map! do |x|
    if x.class == Hash
      x = x.to_a
    else
      x = x
    end
  end
  jsonary.flatten!
end

sum = 0
jsonary.each { |i| sum+= i.to_i } #any string converted to int is 0 so we don't really need to do any type checking

puts sum
