require 'pry'

#binding.pry

class Light
  attr_reader :bulb
  def initialize(val=0)
    @bulb = val
  end

  def turn_on
    @bulb += 1
  end

  def turn_off
    @bulb = [0,@bulb-1].max
  end

  def toggle
    @bulb += 2
  end

  def ==(other)
    @bulb == other
  end

  def to_i
    @bulb.to_i
  end

  def to_s
    @bulb.to_s
  end

  def +(other)
    if other.is_a? Light
      Light.new(@bulb + other.bulb)
    elsif other.is_a? Integer
      Light.new(@bulb + other)
    else
      raise TypeError, "#{other.class} can't be coerced into Light"
    end
  end

  def coerce(other)
    [Light.new(other), self]
  end
end

instructions = File.readlines('./input', :chomp=> true)
display = Array.new(1000) { Array.new(1000) { Light.new } }

def turn_on(x1, y1, x2, y2, grid)
  grid[y1..y2].each do |i|
    i[x1..x2].each { |j| j.turn_on }
  end
end

def turn_off(x1, y1, x2, y2, grid)
  grid[y1..y2].each do |i|
    i[x1..x2].each { |j| j.turn_off }
  end
end

def toggle(x1, y1, x2, y2, grid)
  grid[y1..y2].each do |i|
    i[x1..x2].each { |j| j.toggle }
  end
end

instructions.each do |i|
  match = i.match(/([\w\s]+) (\d+),(\d+) through (\d+),(\d+)/)
  x1 = match[2].to_i
  y1 = match[3].to_i
  x2 = match[4].to_i
  y2 = match[5].to_i

  case match[1]
  when 'toggle'
    toggle(x1, y1, x2, y2, display)
  when 'turn on'
    turn_on(x1, y1, x2, y2, display)
  when 'turn off'
    turn_off(x1, y1, x2, y2, display)
  end
end

lightcount = 0
display.each { |i| lightcount += i.sum }

puts lightcount
