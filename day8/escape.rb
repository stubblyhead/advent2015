words = File.readlines('./input', :chomp => true)
codelength = 0
charlength = 0

words.each do |i|
  codelength += i.length
  charlength += eval("#{i}").length
end

puts codelength - charlength
