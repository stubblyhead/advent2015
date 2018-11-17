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
