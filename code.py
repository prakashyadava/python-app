t = int(input())
while t>0 :
    k =int(input())
    n = int(input())
    m = int(input())
    n_list = []
    m_list = []

    n_list.append((input()).split())

    m_list.append((input()).split())
    str = []

    for i in range(0,n+m):
        if len(m_list)==0 and len(n_list)!=0:
            print(n_list[0])
            n_list.pop(0)
        elif len(n_list)==0 and len(m_list)!=0:
            print(m_list[0])
            m_list.pop(0)
        elif n_list[0]<=m_list[0] and len(n_list)!=0 and len(m_list)!=0:
            # arr.append(n_list[0])
            print(n_list[0])
            n_list.pop(0)

        elif m_list[0]<=n_list[0] and len(m_list)!=0 and len(m_list)!=0:
            # arr.append(m_list[0])
            print(m_list[0])
            m_list.pop(0)



    print(str)

