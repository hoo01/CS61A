def divide(numbers, range_list):

    # 返回的字典应该是：
# {
#    3: [15, 30],
#    5: [10, 15, 20, 25, 30]
# }
    #return {x:[y for y in range_list if y % x == 0] for x in numbers if x > 2}
    result = {}
    for x in numbers:
        if x > 2:
            result[x] = []

            for y in range_list:
                if y % x == 0:
                    result[x].append(y)

    return result


print(divide([2,3,5],[10,15,20,25,30]))
