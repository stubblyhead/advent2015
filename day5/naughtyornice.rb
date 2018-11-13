def nice?(str)
  if str.match(/(ab)|(cd)|(pq)|(xy)/)
    return false
  else
    if str.match(/.*[aeiou].*[aeiou].*[aeiou].*) and str.match((\w)\1)
      return true
    end
  end
  return false
end

true
