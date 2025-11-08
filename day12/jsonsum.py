import json
import re

if __name__ == '__main__':
    with open('input') as f:
        data = f.readline().strip()

    nums = re.findall(r'-?\d+',data)
    nums = list(map(int,nums))
    print(sum(nums))    