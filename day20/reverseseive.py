from functools import reduce

def get_factors(num):
    return set(reduce(
        list.__add__,
        ([i, num//i] for i in range(1,int(n**0.5)+1) if n%i ==0 )))

    
    


if __name__ == '__main__':

    
    target = 34_000_000

    # houses get 10x the product of unique prime factors, so i need the
    # lowest number with product of unique prime factors less than 
    # 34000000 / 10 = 3400000 = 3.4 million

    
    for n in range(1,int(3_400_000/2)):
        if sum(get_factors(n))*10 >= target:
            print(n)
            break
        # if n % 10000 == 0:
        #     print(n)