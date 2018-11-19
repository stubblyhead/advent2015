require 'matrix'

lines = File.readlines('./testcase', :chomp => true)
ingredients = []
lines.each do |i|
  stats = []
  parts = i.split(',')
  parts.each { |j| stats.push(j.match(/-?\d+/)[0].to_i) }
  ingredients.push(stats)
end

ingredients = Matrix[*(ingredients.transpose)]


puts ingredients * quantities
