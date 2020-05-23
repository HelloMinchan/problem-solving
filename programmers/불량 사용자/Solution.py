def DFS(sj, user_id, banned_id, visit_u, visit_b, stack):
    if len(set(stack)) == len(banned_id):
        answer.append(stack[:])
        return
    
    for i in range(len(user_id)):
        for j in range(sj, len(banned_id)):
            if not visit_u[i] and not visit_b[j] :
                length_ui = len(user_id[i])
                length_bi = len(banned_id[j])
                
                if length_ui != length_bi:
                    continue
                
                isSame = True
                for k in range(length_ui):
                    if user_id[i][k] != banned_id[j][k]:
                        if banned_id[j][k] != "*":
                            isSame = False
                            break
                
                if isSame:
                    visit_b[j] = visit_u[i] = True
                    stack.append(user_id[i])
                    DFS(j, user_id, banned_id, visit_u, visit_b, stack)
                    visit_b[j] = visit_u[i] = False
                    stack.pop()

                    
def solution(user_id, banned_id):
    global answer
    answer = []
    visit_u = [False] * len(user_id)
    visit_b = [False] * len(banned_id)
    stack = []
    
    DFS(0, user_id, banned_id, visit_u, visit_b, stack)
    
    return len(list(set([tuple(sorted(ans)) for ans in answer])))