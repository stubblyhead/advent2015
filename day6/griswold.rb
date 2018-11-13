class Light
  attr_reader :bulb

  def initialize
    @bulb = false
  end

  def turn_on
    @bulb = true
  end

  def turn_off
    @bulb = false
  end

  def toggle
    @bulb = !@bulb
  end
end

mylight = Light.new
mylight.turn_on
puts mylight.bulb
mylight.turn_off
puts mylight.bulb
mylight.toggle
puts mylight.bulb
