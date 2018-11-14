def bobby_and(x,y)
  x & y
end

def bobby_or(x,y)
  x ^ y
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
