voted = {}


def check_voter(name):
    if voted.get(name):
        print("돌려보내세요!")
    else:
        voted[name] = true
        print("투표하게 하세요.")
