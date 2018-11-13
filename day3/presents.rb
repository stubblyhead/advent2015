require 'pry'
#binding.pry

instructions = File.readlines('./input', :chomp=> true)[0]
up_count = instructions.count(?^)
down_count = instructions.count(?v)
left_count = instructions.count(?<)
right_count = instructions.count(?>)

grid = Array.new(up_count + down_count) { Array.new(left_count + right_count) { 0 } }
x = left_count
y = up_count
grid[y][x] = 1
housecount = 1

instructions.each_char do |i|
  case i
  when ?>
    x += 1
  when ?<
    x -= 1
  when ?v
    y += 1
  when ?^
    y -= 1
  end
  if grid[y][x] == 0
    housecount += 1
  end
  grid[y][x] += 1
end
puts housecount
