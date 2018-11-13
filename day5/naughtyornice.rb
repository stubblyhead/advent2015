require 'pry'
#binding.pry

def nice?(str)
  if str.match(/(ab)|(cd)|(pq)|(xy)/)
    return false
  else
    if str.match /.*[aeiou].*[aeiou].*[aeiou].*/ and str.match /(\w)\1/
      return true
    end
  end
  return false
end

def nice2?(str)
  if str.match(/(..).*\1/) and str.match(/(.).\1/)
    return true
  else
    return false
  end
end
words = File.readlines('./input', :chomp=>true)

nicecount = 0
nicecount2 = 0

words.each do |i|
  nicecount += 1 if nice?(i)
  nicecount2 += 1 if nice2?(i)
end

puts "part 1 count #{nicecount}"
puts "part 2 count #{nicecount2}"
