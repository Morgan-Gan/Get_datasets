

def IOU(box1, box2):
    w = max(0, min(box1[2], box2[2]) - max(box1[0], box2[0]))
    h = max(0, min(box1[3], box2[3]) - max(box1[1], box2[1]))
    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    iou = abs(w)*abs(h) / (area1 + area2 - w*h)
    # return h
    return iou

def iou(rect1, rect2):
    xmin1, ymin1, xmax1, ymax1 = rect1
    xmin2, ymin2, xmax2, ymax2 = rect2
    s1 = (xmax1 - xmin1) * (ymax1 - ymin1)
    s2 = (xmax2 - xmin2) * (ymax2 - ymin2)

    sum_area = s1 + s2

    left = max(xmin2, xmin1)
    right = min(xmax2, xmax1)
    top = max(ymin2, ymin1)
    bottom = min(ymax2, ymax1)

    if left >= right or top >= bottom:
        return 0

    intersection = (right - left) * (bottom - top)
    return intersection / (sum_area - intersection ) * 1.0




if __name__ == '__main__':
    box1 = [1, 2, 3, 4]
    box2 = [2, 2, 3, 4]
    # result = IOU(box1, box2)
    result = iou(box1, box2)
    print(result)
