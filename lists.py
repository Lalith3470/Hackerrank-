if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        l=list(map(str,input().split()))
        if l[0]=="insert":
            l[1]=int(l[1])
            l[2]=int(l[2])
            lst.insert(l[1],l[2])
        elif l[0]=="append":
            l[1]=int(l[1])
            lst.append(l[1])
        elif l[0]=="print":
            print(lst)
        elif l[0]=="sort":
            lst.sort()
        elif l[0]=="pop":
            lst.pop()
        elif l[0]=="remove":
            lst.remove(int(l[1]))
        elif l[0]=="reverse":
            lst=lst[::-1]
    
