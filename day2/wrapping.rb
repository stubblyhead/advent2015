packages = File.readlines('./input', :chomp=> true)
area = 0
length = 0
packages.each do |dimensions|
  dimensions = dimensions.split('x')
  dimensions.each_index { |i| dimensions[i] = dimensions[i].to_i }
  length += dimensions[0] * dimensions[1] * dimensions[2]
  area += 2*dimensions[0]*dimensions[1] + 2*dimensions[0]*dimensions[2] + 2*dimensions[1]*dimensions[2]
  dimensions.sort!.pop
  length += 2*(dimensions[0] + dimensions[1])
  area += dimensions[0] * dimensions[1]
end
puts "#{area} sqft of papaer"
puts "#{length} feet of ribbon"
