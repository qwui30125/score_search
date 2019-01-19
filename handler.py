def getScores():
    with open("2018秋七年级学生成绩1.17.csv") as f:
        lines = f.readlines()
        title = lines[0].strip().split(",")
        scores = []
        for line in lines[1:]:
            stu_score = line.strip().split(",")
            scores.append(stu_score)
    return title, scores


def createMap(title, scores):
    # 班级,考号,姓名,总分,语文,数学,英语,笔试,口语,政治,历史,地理,生物,禁毒,总分
    # 701,2018012529,朱可欣,531,108,113,114,100,14,47,41,48,50,10,531
    title_e = ["stu_class", "stu_id", "stu_name", "scor_total", 
    "scor_chinese", "scor_math", "scor_english", "scor_written", "scor_speaking", 
    "scor_political", "scor_history", "scor_geography",
    "scor_biological", "scor_antidrug", "scor_total"]
    title_map = {}
    score_map = {}
    for t_c, t_e in zip(title, title_e):
        title_map[t_e] = t_c

    for score in scores:
        d = {}
        for i in range(len(score)):
            d[title_e[i]] = score[i]
        score_map[d["stu_id"]] = d
    print(title_map)
    print(score_map["2018012529"])
        
    return title_map, score_map


def main():
    title, scores = getScores()
    for t, s in zip(title, scores[0]):
        print("%s:%s" % (t, s))
    print(title)
    print(scores[0])
    title_map, score_map = createMap(title, scores)

    name = input("请输入姓名：")
    stu_id = input("请输入学号：")
    
    score = score_map.get(stu_id, None)
    if not score:
        print("学号错误")
        return

    if score["stu_name"] != name:
        print("学号与姓名不匹配")
        return

    print(score)

    




if __name__ == "__main__":
    main()