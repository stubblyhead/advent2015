import json
import re

def obj_hook(s):
    if 'red' in s.values():
        return {}
    else:
        return s

if __name__ == '__main__':
    with open('input') as f:
        data = f.readline().strip()

    nums = re.findall(r'-?\d+',data)
    nums = list(map(int,nums))
    print(sum(nums))

    json_data = json.loads(data,object_hook=obj_hook)
    no_red = json.dumps(json_data)
    nums = re.findall(r'-?\d+', no_red)
    nums = list(map(int,nums))
    print(sum(nums))