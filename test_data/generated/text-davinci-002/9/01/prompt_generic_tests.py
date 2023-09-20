def function(dictionary, start):
    # Your code here
    visited_list = []
    visited_list.append(start)

    for i in range(len(dictionary[start])):
        if dictionary[start][i] not in visited_list:
            visited_list.append(dictionary[start][i])
            for j in range(len(dictionary[dictionary[start][i]])):
                if dictionary[dictionary[start][i]][j] not in visited_list:
                    visited_list.append(dictionary[dictionary[start][i]][j])

    return visited_list