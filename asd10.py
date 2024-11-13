class Box:
    def __init__(self, sides):
        self.sides = sorted(sides)
        self.capacity = 0
    def can_nest(self, other):
        return all(self.sides[i] <= other.sides[i] for i in range(len(self.sides)))

def nested_boxes_lis(boxes):
    lis = []
    for i in range(len(boxes)):
        n = 0
        for j in range(i, len(boxes)):
            if boxes[i].can_nest(boxes[j]):
                n += 1
        boxes[i].capacity = n
    boxes.sort(key=lambda box:box.capacity,reverse=True)
    if boxes:
        lis.append(boxes[0])
        for i in range(1, len(boxes)):
            if lis[-1].can_nest(boxes[i]):
                lis.append(boxes[i])
    return len(lis)

with open('input.txt', 'r') as file:
    dim, count = map(int, file.readline().split())
    boxes = [Box(list(map(int, file.readline().split()))) for _ in range(count)]
result = nested_boxes_lis(boxes)
with open('output.txt', 'w') as output_file:
    output_file.write(str(result))
print(result)
