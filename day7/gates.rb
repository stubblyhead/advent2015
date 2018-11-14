require 'pry'
#binding.pry

def bobby_and(x,y)
  x & y
end

def bobby_or(x,y)
  x | y
end

def bobby_lshift(x,y)
  x << y
end

def bobby_rshift(x,y)
  x >> y
end

def bobby_not(x)
  65535 - x
end

gates = {}

instructions = File.readlines('./input', :chomp => true)
def ready?(x, gates)
  x = x.split
  if x.length == 1
    x[0].match(/\d+/) ? x = x[0].to_i : x = gates[x[0]]
    x
  elsif x.length == 2
    x[1].match(/\d+/) ? x = x[1].to_i : x = gates[x[1]]
    x
  else
    x[2].match(/\d+/) ? y = x[2].to_i : y = gates[x[2]]
    x[0].match(/\d+/) ? x = x[0].to_i : x = gates[x[0]]
    x and y
  end
end

while instructions.length > 0
  instructions.each do |i|
    lside, rside = i.split(' -> ')
    if ready?(lside, gates)
      x = lside.split
      operation = x[1]
      case x.length
      when 1
        x[0].match(/\d+/) ? x = x[0].to_i : x = gates[x[0]]
        gates[rside] = x
      when 2
        x[1].match(/\d+/) ? x = x[1].to_i : x = gates[x[1]]
        gates[rside] = bobby_not(x)
      else
        x[2].match(/\d+/) ? y = x[2].to_i : y = gates[x[2]]
        x[0].match(/\d+/) ? x = x[0].to_i : x = gates[x[0]]
        case operation
        when 'AND'
          gates[rside] = bobby_and(x,y)
        when 'OR'
          gates[rside] = bobby_or(x,y)
        when 'LSHIFT'
          gates[rside] = bobby_lshift(x,y)
        when 'RSHIFT'
          gates[rside] = bobby_rshift(x,y)
        end
      end
      instructions.delete(i)
    end
  end
end

puts gates['a']
