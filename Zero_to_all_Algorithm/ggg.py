def solution(info, query):
    info_all = []
    query_all = []

    for x in info:
        info_all.append(x.split())

    for x in query:
        query_all.append(x.split())

    answer = [0 for _ in range(len(query_all))]
    for i in range(len(query_all)):
        for j in range(3):
            query_all[i].remove('and')

    for i in range(len(query_all)):
        for j in range(len(info_all)):
            count = 0
            for k in range(4):
                if info_all[j][k] == query_all[i][k] or query_all[i][k] == '-':
                    count += 1
                else:
                    count = 0

            if count == 4 and int(query_all[i][-1]) <= int(info_all[j][-1]):
                answer[i] += 1

    return answer



info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))
print(info[0].split())