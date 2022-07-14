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
            print(i)
        print('Done !')
    elif x == 3:
        print('Checking available proxies ...')
        proxy2 = [FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get()]
        for i in proxy2:
            print(i)
        print('Done !')
    elif x == 4:
        print('Checking available proxies ...')
        prox = [FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get()]
        for i in prox:
            print(i)
        print('Done !')
    elif x == 5:
        print('Checking available proxies ...')
        pro = [FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get(), FreeProxy(rand=True).get()]
        for i in pro:
            print(i)
        print('Done !')
    elif x == 0:
        print('Why would you want to get 0 proxies ? ')
    elif x > 5:
        print('Five is the limit bro ...')

except ValueError:
    print('Maybe next time try to put an integer ?')