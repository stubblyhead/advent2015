directions = File.readlines('./input', :chomp=>true)[0]

floor = 0
floor += directions.count(?() - directions.count(?))

puts "floor #{floor}"

floor = 0
directions.chars.each_index do |i|
  case directions[i]
  when '('
    floor += 1
  when ')'
    floor -= 1
  end
  if floor < 0
    puts "position #{i + 1}"
    break
  end
end
