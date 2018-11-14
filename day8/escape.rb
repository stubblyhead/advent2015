words = File.readlines('./input', :chomp => true)
codelength = 0
charlength = 0
encodedlength = 0

words.each do |i|
  codelength += i.length
  charlength += eval("#{i}").length
  encodedlength += i.inspect.length
end

puts codelength - charlength
puts encodedlength - codelength
