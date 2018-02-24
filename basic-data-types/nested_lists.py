if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    sorted_students  = sorted(set(x[1] for x in students))
    for name in sorted(i[0] for i in students if i[1] == sorted_students[1]):
        print(name)
