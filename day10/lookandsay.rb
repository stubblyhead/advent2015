require 'pry'
binding.pry

def lookandsay(str)
  num_ary = str.chars
  outstr = ''
  current_num = 0
  next_num = 0
  while num_ary.length > 0
    current_num = num_ary.shift.to_i
    current_count = 1
    while num_ary[0].to_i == current_num
      current_count += 1
      num_ary.shift
    end
    outstr = outstr + current_count.to_s + current_num.to_s
  end
  outstr
end

puts lookandsay('21')
