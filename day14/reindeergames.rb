class Reindeer
  attr_reader :speed, :run_time, :rest_time, :distance

  def initialize(speed, run_time, rest_time)
    @speed = speed
    @run_time = run_time
    @rest_time = rest_time
  end

  def run(time)
    cycles = time / (@run_time + @rest_time)
    leftover = time % (@run_time + @rest_time)
    @distance = cycles * @speed * @run_time
    @distance += [@run_time, leftover].min * speed
  end

end
field = {}
lines = File.readlines('./input', :chomp => true)
lines.each do |i|
  match = i.match(/^(\w+).* (\d+).* (\d+).* (\d+)/)
  name, speed, run, rest = match[1,4]
  field[name] = Reindeer.new(speed.to_i, run.to_i, rest.to_i)
end

field.each_value { |i| i.run(2503) }

results = field.values
results.map! { |i| i = i.distance }

puts results.max
