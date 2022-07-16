from fp.fp import FreeProxy
try:
    x = int(input('How many proxies do you want to get [1-5] ? '))

    if x == 1:
        print('Checking available proxies ...')
        proxy = FreeProxy(rand=True).get()
        print(proxy)
        print('Done !')
    elif x == 2:
        print('Checking available proxies ...')
        proxy_list1 = [FreeProxy(rand=True).get(), FreeProxy(rand=True).get()]
        for i in proxy_list1:
            if [1] in proxy_list1 == [0]:
                proxy_list1.remove([0])
                proxy_list1.append(FreeProxy(rand=True).get())
            print(i)
        print('Done !')
    elif x == 3:
        print('Checking available proxies ...')
        proxy2 = [FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get()]
        proxy2set = set(proxy2)
        for i in proxy2:
            if len(proxy2) == len(proxy2set):
                print(i)
            else:
                proxy2.append(FreeProxy(rand=True).get())
                print(i)
        print('Done !')
    elif x == 4:
        print('Checking available proxies ...')
        prox = [FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get()]
        proxset = set(prox)
        for i in prox:
            if len(prox) == len(proxset):
                print(i)
            else:
                prox.append(FreeProxy(rand=True).get())
                print(i)
        print('Done !')
    elif x == 5:
        print('Checking available proxies ...')
        pro = [FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get()]
        proset = set(pro)
        for i in pro:
            if len(pro) == len(proset):
                print(i)
            else:
                pro.append(FreeProxy(rand=True).get())
                print(i)
            print('Done !')
    elif x == 0:
        print('Why would you want to get 0 proxies ? ')
    elif x > 5:
        print('Five is the limit bro ...')

except ValueError:
    print('Maybe next time try to put an integer ?')