def southeast(grim,i,j,former_i,former_j,patha):
    if 0 <= i+1 < len(grim) and 0 <= j+1 < len(grim[i+1]) and grim[i+1][j+1] != 0 and (former_i != i+1 or former_j != j+1):
        if [i+1,j+1] == default[0]:
            return patha
        for k in default:
            if k == [i+1,j+1]:
                break
        else:
            ahead = go_next(grim,i+1,j+1,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def south(grim,i,j,former_i,former_j,patha):
    if 0 <= i+1 < len(grim) and 0 <= j < len(grim[i+1]) and grim[i+1][j] != 0 and (former_i != i+1 or former_j != j):
        if [i+1,j] == default[0]:
            return patha
        for k in default:
            if k == [i+1,j]:
                break
        else:
            ahead = go_next(grim,i+1,j,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def southwest(grim,i,j,former_i,former_j,patha):
    if 0 <= i+1 < len(grim) and 0 <= j-1 < len(grim[i+1]) and grim[i+1][j-1] != 0 and (former_i != i+1 or former_j != j-1):
        if [i+1,j-1] == default[0]:
            return patha
        for k in default:
            if k == [i+1,j-1]:
                break
        else:
            ahead = go_next(grim,i+1,j-1,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def west(grim,i,j,former_i,former_j,patha):
    if 0 <= i < len(grim) and 0 <= j-1 < len(grim[i]) and grim[i][j-1] != 0 and (former_i != i or former_j != j-1):
        if [i,j-1] == default[0]:
            return patha
        for k in default:
            if k == [i,j-1]:
                break
        else:
            ahead = go_next(grim,i,j-1,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def northwest(grim,i,j,former_i,former_j,patha):
    if 0 <= i-1 < len(grim) and 0 <= j-1 < len(grim[i-1]) and grim[i-1][j-1] != 0 and (former_i != i-1 or former_j != j-1):
        if [i-1,j-1] == default[0]:
            return patha
        for k in default:
            if k == [i-1,j-1]:
                break
        else:
            ahead = go_next(grim,i-1,j-1,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def north(grim,i,j,former_i,former_j,patha):
    if 0 <= i-1 < len(grim) and 0 <= j < len(grim[i-1]) and grim[i-1][j] != 0 and (former_i != i-1 or former_j != j):
        if [i-1,j] == default[0]:
            return patha
        for k in default:
            if k == [i-1,j]:
                break
        else:
            ahead = go_next(grim,i-1,j,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def northeast(grim,i,j,former_i,former_j,patha):
    if 0 <= i-1 < len(grim) and 0 <= j+1 < len(grim[i]) and grim[i-1][j+1] != 0 and (former_i != i-1 or former_j != j+1):
        if [i-1,j+1] == default[0]:
            return patha
        for k in default:
            if k == [i-1,j+1]:
                break
        else:
            ahead = go_next(grim,i-1,j+1,i,j)
            if ahead:
                patha = patha + ahead
                return patha

def east(grim,i,j,former_i,former_j,patha):
    if 0 <= i < len(grim) and 0 <= j+1 < len(grim[i]) and grim[i][j+1] != 0 and (former_i != i or former_j != j+1):
        if [i,j+1] == default[0]:
            return patha
        for k in default:
            if k == [i,j+1]:
                break
        else:
            ahead = go_next(grim,i,j+1,i,j)
            if ahead:
                patha = patha + ahead
                return patha


def find_all_path(grim):
    path_collection = []
    for i in range(len(grim)):
        for j in range(len(grim[i])):
            single_path = find_path_with_start_point(grim, i, j)
            if single_path:
                path_collection.append(single_path)
                for k in single_path:
                    grim[k[0]][k[1]] = 0
    return path_collection


def find_path_with_start_point(grim, i, j):
    global default
    default = []
    if grim[i][j] == 0:
        return
    else:
        global highest_height
        highest_height = i
        path = [[i, j]]
        if 0 <= i < len(grim) and 0 <= j + 1 < len(grim[i]) and grim[i][j + 1] != 0:
            ahead = go_next(grim, i, j + 1, i, j)
            if ahead:
                path = path + ahead
                return path
        if 0 <= i + 1 < len(grim) and 0 <= j + 1 < len(grim[i]) and grim[i + 1][j + 1] != 0:
            ahead = go_next(grim, i + 1, j + 1, i, j)
            if ahead:
                path = path + ahead
                return path
        if 0 <= i + 1 < len(grim) and 0 <= j < len(grim[i]) and grim[i + 1][j] != 0:
            ahead = go_next(grim, i + 1, j, i, j)
            if ahead:
                path = path + ahead
                return path
        if 0 <= i + 1 < len(grim) and 0 <= j - 1 < len(grim[i]) and grim[i + 1][j - 1] != 0:
            ahead = go_next(grim, i + 1, j - 1, i, j)
            if ahead:
                path = path + ahead
                return path
        return



def go_next(grim, i, j, former_i, former_j):
    if 0 <= i < len(grim) and 0 <= j < len(grim[i]):
        if grim[i][j] == 0:
            return
        else:
            default.append([former_i, former_j])
            # print('default:',default)
            patha = [[i, j]]
            # sub_point is at the same level with start_point.
            if i == highest_height:

                if 0 <= i < len(grim) and 0 <= j+1 < len(grim[i]) and grim[i][j+1] != 0:
                    for k in default:
                        if k == [i, j+1]:
                            break
                    else:
                        ahead = go_next(grim, i, j+1, i, j)
                        if ahead:
                            patha = patha + ahead
                            return patha

                if 0 <= i+1 < len(grim) and 0 <= j+1 < len(grim[i+1]) and grim[i+1][j+1] != 0:
                    for k in default:
                        if k == [i+1, j+1]:
                            break
                    else:
                        ahead = go_next(grim, i+1, j+1, i, j)
                        if ahead:
                            patha = patha + ahead
                            return patha

                ahead = highest_height_path_search(grim, i + 1, j, i, j, patha)
                if 0 <= i+1 < len(grim) and 0 <= j < len(grim[i+1]) and grim[i+1][j] != 0:
                    for k in default:
                        if k == [i+1, j]:
                            break
                    else:
                        ahead = go_next(grim, i+1, j, i, j)
                        if ahead:
                            patha = patha + ahead
                            return patha

                ahead = highest_height_path_search(grim, i + 1, j - 1, i, j, patha)
                if 0 <= i+1 < len(grim) and 0 <= j-1 < len(grim[i+1]) and grim[i+1][j-1] != 0:
                    for k in default:
                        if k == [i+1, j-1]:
                            break
                    else:
                        ahead = go_next(grim, i+1, j-1, i, j)
                        if ahead:
                            patha = patha + ahead
                            return patha
                return
            else:
                if i - 1 == former_i and j == former_j:
                    southeast(grim, i, j, former_i, former_j, patha)
                    south(grim, i, j, former_i, former_j, patha)
                    southwest(grim, i, j, former_i, former_j, patha)
                    west(grim, i, j, former_i, former_j, patha)
                    northwest(grim, i, j, former_i, former_j, patha)
                    return
                elif i - 1 == former_i and j + 1 == former_j:
                    southeast(grim, i, j, former_i, former_j, patha)
                    south(grim, i, j, former_i, former_j, patha)
                    southwest(grim, i, j, former_i, former_j, patha)
                    west(grim, i, j, former_i, former_j, patha)
                    northwest(grim, i, j, former_i, former_j, patha)
                    north(grim, i, j, former_i, former_j, patha)
                    return
                elif i == former_i and j + 1 == former_j:
                    southwest(grim, i, j, former_i, former_j, patha)
                    west(grim, i, j, former_i, former_j, patha)
                    northwest(grim, i, j, former_i, former_j, patha)
                    north(grim, i, j, former_i, former_j, patha)
                    northeast(grim, i, j, former_i, former_j, patha)
                    return
                elif i + 1 == former_i and j + 1 == former_j:
                    southwest(grim, i, j, former_i, former_j, patha)
                    west(grim, i, j, former_i, former_j, patha)
                    northwest(grim, i, j, former_i, former_j, patha)
                    north(grim, i, j, former_i, former_j, patha)
                    northeast(grim, i, j, former_i, former_j, patha)
                    east(grim, i, j, former_i, former_j, patha)
                    return
                elif i + 1 == former_i and j == former_j:
                    northwest(grim, i, j, former_i, former_j, patha)
                    north(grim, i, j, former_i, former_j, patha)
                    northeast(grim, i, j, former_i, former_j, patha)
                    east(grim, i, j, former_i, former_j, patha)
                    southeast(grim, i, j, former_i, former_j, patha)
                    return
                elif i + 1 == former_i and j - 1 == former_j:
                    northwest(grim, i, j, former_i, former_j, patha)
                    north(grim, i, j, former_i, former_j, patha)
                    northeast(grim, i, j, former_i, former_j, patha)
                    east(grim, i, j, former_i, former_j, patha)
                    southeast(grim, i, j, former_i, former_j, patha)
                    south(grim, i, j, former_i, former_j, patha)
                    return
                elif i == former_i and j - 1 == former_j:
                    northeast(grim, i, j, former_i, former_j, patha)
                    east(grim, i, j, former_i, former_j, patha)
                    southeast(grim, i, j, former_i, former_j, patha)
                    south(grim, i, j, former_i, former_j, patha)
                    southwest(grim, i, j, former_i, former_j, patha)
                    return
                else:
                    northeast(grim, i, j, former_i, former_j, patha)
                    east(grim, i, j, former_i, former_j, patha)
                    southeast(grim, i, j, former_i, former_j, patha)
                    south(grim, i, j, former_i, former_j, patha)
                    southwest(grim, i, j, former_i, former_j, patha)
                    west(grim, i, j, former_i, former_j, patha)
                    return
                return
    else:
        return