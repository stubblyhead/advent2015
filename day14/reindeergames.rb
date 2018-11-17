require 'pry'
binding.pry

class Reindeer
  attr_reader :speed, :run_time, :rest_time, :distance, :elapsed_time, :points

  def initialize(speed, run_time, rest_time)
    @speed = speed
    @run_time = run_time
    @rest_time = rest_time
    @elapsed_time = 0
    @distance = 0
    @points = 0
  end

  def running?
    @elapsed_time % (@run_time + @rest_time) < @run_time
  end

  def add_point
    @points += 1
  end

  def run
    @distance += @speed if running?
    @elapsed_time += 1
  end

end
field = []
lines = File.readlines('./input', :chomp => true)
lines.each do |i|
  match = i.match(/.* (\d+).* (\d+).* (\d+)/)
  speed, run, rest = match[1,3]
  field.push (Reindeer.new(speed.to_i, run.to_i, rest.to_i))
end

2503.times { |t|
  distances = field.map do |i|
    i.run
    i.distance
  end
  max_distance = distances.max
  distances.each_with_index do |x,i|
    if x == max_distance
      field[i].add_point
    end
  end
}

puts field.map { |i| i.points }.max
