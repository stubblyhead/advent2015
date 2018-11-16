def valid?(str)
  return false if str.match(/i|l|o/) #any pw with these letters is invalid
  match = str.match(/(\w)\1/)
  if match
    double = str.index(match[1]) #find where double letter starts
    temp = str[0..double] + str[double+2..-1] #get candidate without the double letter
    return false unless !temp.match(match[1]) and temp.match(/(/w)\1/) #bail early unless
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
