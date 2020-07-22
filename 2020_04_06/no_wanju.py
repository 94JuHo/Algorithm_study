def solution(participant, completion):
    #참가 선수는 1명 이상 100,000명 이하 
    if 1 > len(participant) or len(participant) > 100000:
        return 0
    #completion의 길이는 participant의 길이보다 1 작음 
    if len(participant)-1 != len(completion):
        return 0

    for name in participant:
        # 이름이 알파벳이 아니고 길이가 1과 20사이가 아니면 종료 
        if not name.isalpha():
            if not len(name)>= 1 and len(name) <= 20:
                return 0
        ####
        for c_name in completion:
            if name == c_name:
                print(name)
                participant.remove(name)
                completion.remove(name)
    
    answer = participant
    return answer

#참가자 수는 1명 이상 100,000명 이하
#이름은 알파벳 소문자 1 <= X <= 20
#동명이인 존재할 수 있음
participant = ["mislav", "stanko", "mislav", "ana"]

#len(completion) == len(participant)-1
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))