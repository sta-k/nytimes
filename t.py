def a():
    from myapp.models import News
    import datetime
    import json
    print(News.objects.all().delete())
    file_not_found=open('file_not_found.txt','w')
    for year in range(1856,1950):
        for m in range(1,13):
            print(f'{m}_{year}.json')
            try:                
                temp=open(f'staticfiles/{m}_{year}.json')
            except:
                print('file not found',f'{m}_{year}.json')
                file_not_found.write(f'{m}_{year}.json')
            else:
                with open(f'staticfiles/{m}_{year}.json') as f:
                    d = json.load(f)
                    news = []
                    for k,v in d.items():
                        try:
                            newDate = datetime.datetime(int(k[-4:]),int(k[2:4]),int(k[:2]))
                        except ValueError:
                            print(f'Date Error:{k}')
                        for t in v:
                            if '<!DOCTYPE html>' in t: 
                                continue
                            news.append(News(ndate=newDate,title=t))
                    News.objects.bulk_create(news)

def b():
    for i in range(10):
        try:
            x=1/i
        except:
            print('cannot divided by zero')
        else:
            print(1/i)
        finally:
            print('finaly')
        print('='*10)
b()