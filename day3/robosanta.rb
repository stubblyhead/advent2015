instructions = File.readlines('./input', :chomp=> true)[0]
up_count = instructions.count(?^)
down_count = instructions.count(?v)
left_count = instructions.count(?<)
right_count = instructions.count(?>)

grid = Array.new(up_count + down_count) { Array.new(left_count + right_count) { 0 } }
santa_x = left_count
santa_y = up_count
robo_x = left_count
robo_y = up_count

grid[santa_y][robo_x] = 2
housecount = 1

instructions.chars.each_index do |i|
  case instructions[i]
  when ?>
    if i.odd?
      santa_x += 1
    else
      robo_x += 1
    end
  when ?<
    if i.odd?
      santa_x -= 1
    else
      robo_x -= 1
    end
  when ?^
    if i.odd?
      santa_y -= 1
    else
      robo_y -= 1
    end
  when ?v
    if i.odd?
      santa_y += 1
    else
      robo_y += 1
    end
  end

  if i.odd?
    housecount += 1 if grid[santa_y][santa_x] == 0
    grid[santa_y][santa_x] += 1
  else
    housecount += 1 if grid[robo_y][robo_x] == 0
    grid[robo_y][robo_x] += 1
  end
end

puts housecount
