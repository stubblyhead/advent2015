def valid?(str)
  return false if str.match(/i|l|o/) #any pw with these letters is invalid
  match = str.match(/(\w)\1/)
  if match
    double = str.index(match[0]) #find where double letter starts
    temp = str.sub(match[0], '--') #replace double letter with non-alphanumeric chars
    return false unless !temp.match(match[0]) and temp.match(/(\w)\1/) #bail early unless
    #candidate doesn't contain the first double letter and does contain a different double letter
  else
    return false  #no double letters at all
  end
  if str.match(/abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz/)
    return true
  else
    return false
  end
end

password = 'vzbxkghb'
valid = false
until valid
  password.succ!
  valid = valid?(password)
end

puts password
