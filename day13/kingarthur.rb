lines = File.readlines('./input', :chomp=>true)
guests = []
happiness_rules = {}

lines.each do |i|
  i.sub!('gain', '')  #do some minor line edits for easier regex
  i.sub!('lose ', '-')
  match = i.match(/^(\w+).* (-?\d+).* (\w+).$/)  #grab the names on either end and the happiness modifier in the middle
  current,happy,neighbor = match[1,3]
  happiness_rules[[current,neighbor]] = happy.to_i  #hash of [current_person, neighbor] => happiness modifier
  guests.push(current)  #will result in a lot of dupes, but it's easier to add them all now and sort it out later
end

guests.uniq!

max_happiness = -Float::INFINITY

guests.permutation.each do |i|
  this_happiness = 0
  i.each_index do |curr|
    left_neighbor = (curr+1) % i.length
    right_neighbor = curr-1
    this_happiness += happiness_rules[[i[curr],i[left_neighbor]]] + happiness_rules[[i[curr],i[right_neighbor]]]
  end
  max_happiness = [max_happiness, this_happiness].max
end

puts "part 1 #{max_happiness}"

guests.each do |i|
  happiness_rules[['me',i]] = 0
  happiness_rules[[i,'me']] = 0
end
guests.push('me')

max_happiness = -Float::INFINITY

guests.permutation.each do |i|
  this_happiness = 0
  i.each_index do |curr|
    left_neighbor = (curr+1) % i.length
    right_neighbor = curr-1
    this_happiness += happiness_rules[[i[curr],i[left_neighbor]]] + happiness_rules[[i[curr],i[right_neighbor]]]
  end
  max_happiness = [max_happiness, this_happiness].max
end

puts "part 2 #{max_happiness}"
