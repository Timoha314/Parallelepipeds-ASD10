def UpperBound(a, x):
    l = 0
    r = len(a)
    while l < r:
        k = (l + r) // 2
        if x < a[k]:
            r = k
        else:
            l = k + 1
    return l

def LIS(sequence):
    lis = []
    for num in sequence:
        pos = UpperBound(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    return len(lis)

def nested_boxes_lis(boxes, dim):
    for i in range(len(boxes)):
        boxes[i].sort()
    boxes.sort()
    lis_values = []
    for i in range(dim):
        columns = [boxes[row][i] for row in range(len(boxes))]
        lis_length = LIS(columns)
        lis_values.append(lis_length)
    return min(lis_values)

with open('input.txt', 'r') as file:
    dim, count = map(int, file.readline().split())
    boxes = [list(map(int, file.readline().split())) for _ in range(count)]
result = nested_boxes_lis(boxes, dim)
with open('output.txt', 'w') as output_file:
    output_file.write(str(result))

print(result)
