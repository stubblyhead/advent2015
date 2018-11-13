require 'digest'

unless key = ARGV[0] #this is deliberate
  puts "please pass the puzzle input"
  exit
end

count = 1
while true
  coinhash = Digest::MD5.hexdigest(key + count.to_s)
  if coinhash[0,6] == '000000'
    puts count
    exit
  end
  count += 1
end
