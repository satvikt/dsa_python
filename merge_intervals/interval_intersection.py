"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
"""









def merge(intervals_a, intervals_b):
    result = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        # a is engulfed in b or a ends after b
        a_overlaps_b = intervals_a[i][start] >= intervals_b[j][start] and \
                       intervals_a[i][start] <= intervals_b[j][end]

        b_overlaps_a = intervals_b[j][start] >= intervals_a[i][start] and \
                        intervals_b[j][start] <= intervals_a[i][end]

        if a_overlaps_b or b_overlaps_a:
            overlap_interval = [max(intervals_a[i][start], intervals_b[j][start]), min(intervals_a[i][end], intervals_b[j][end])]
            result.append(overlap_interval)


        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return result

def main():
    # print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    # print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))
    print("Intervals Intersection: " + str(merge([[1, 3]],[[2,4]])))

main()