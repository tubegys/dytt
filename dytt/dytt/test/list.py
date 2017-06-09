urls = ['/html/gndy/dyzz/20170530/54108.html',
 '/html/gndy/dyzz/20170529/54098.html',
 '/html/gndy/dyzz/20170528/54093.html',
 '/html/gndy/dyzz/20170528/54092.html',
 '/html/gndy/dyzz/20170524/54065.html',
 '/html/gndy/dyzz/20170524/54064.html',
 '/html/gndy/dyzz/20170523/54056.html',
 '/html/gndy/dyzz/20170523/54055.html',
 '/html/gndy/dyzz/20170522/54046.html',
 '/html/gndy/dyzz/20170522/54045.html',
 '/html/gndy/dyzz/20170520/54035.html',
 '/html/gndy/dyzz/20170520/54034.html',
 '/html/gndy/dyzz/20170519/54028.html',
 '/html/gndy/dyzz/20170519/54027.html',
 '/html/gndy/dyzz/20170519/54026.html',
 '/html/gndy/dyzz/20170518/54019.html',
 '/html/gndy/dyzz/20170518/54018.html',
 '/html/gndy/dyzz/20170516/54003.html',
 '/html/gndy/dyzz/20170514/53986.html',
 '/html/gndy/dyzz/20170514/53985.html',
 '/html/gndy/dyzz/20170512/53973.html',
 '/html/gndy/dyzz/20170512/53972.html',
 '/html/gndy/dyzz/20170511/53967.html',
 '/html/gndy/dyzz/20170510/53954.html',
 '/html/gndy/dyzz/20170508/53940.html',
 'list_23_2.html',
 'list_23_3.html',
 'list_23_4.html',
 'list_23_5.html',
 'list_23_6.html',
 'list_23_7.html',
 'list_23_2.html',
 'list_23_161.html']


del_urls = []
for url in urls:
    if 'list' in url:
        # print(url)
        del_urls.append(url)

urls = list(set(urls) - set(del_urls))
print(urls)