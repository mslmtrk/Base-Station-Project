"""
Müslüm Türk
Program that finds the base station combination that gives the maximum profit with Dynamic Programming algorithm
"""
import csv
from timeit import default_timer as timer

def max(a, b):
    return a if a>b else b

def dynamicProgramming(m, p, x):
    n = len(m)
    lis = []
    init_max = p[0]
    for i in range(n):#İlk elemana x kadar uzaklıkta olmayan elemanlar aşağıdaki döngüde koşula giremeyecekleri için aralarındaki max'la başlatılır
        if not(m[i] - m[0] >= x):
            init_max = max(init_max, p[i])
            lis.append(init_max)
            continue
        lis.append(p[i]) #Diğer elemanlar normal kar değerini alır

    for i in range(1,n):
        for j in range(i-1, -1, -1):#Her bir indexten geriye doğru giderek aralarında x mesafe olan ilk indexin ya da bir öncekinin değerini i indexine atar
            if (m[i]-m[j]) >= x:
                lis[i] = max(lis[i] + lis[j], lis[i-1]) #Böylece o indexe kadar olan max kar bulunur
                break
            
    stations = []
    i = n-1
    while(i >= 0):
        if lis[i] > lis[i-1]:#lis kendinden öncekinden büyükse stations'a eklenir(bu index maxtoplama eklendiği için)
            stations.append(m[i])
            j=i
            while not(m[i] - m[j] >= x):# x mesafede en yakın istasyona gider
                j -= 1
                if(j==0):#0 kontrol
                    if m[i] - m[j] >= x:
                        stations.append(m[j])
                    break
            if(j == 0):
                break
                        
            i = j
            continue

        elif lis[i] == lis[i-1]:#lis kendinden öncekine eşitse eşit olmayana kadar döner(değerini bir öncekinden aldığı için)
            while lis[i] == lis[i-1]:
                i -= 1
                if i==0:#0 kontrol
                    stations.append(m[i])
                    break
            continue

        i-=1

    stations.sort()
    print("İstasyonların merkeze uzaklıkları:", stations)
    return lis[n-1]

def csv_to_list(filename):#csv dosyalarını okumak için
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)


######################################################################################

m1 = csv_to_list("Dist_on.csv")#10 değeri için çalışır
m = []
sum = 0
for i in range(len(m1)):
    for j in m1[i]:
        sum += int(j)
        m.append(sum)


p1 = csv_to_list("Kar_on.csv")
p = []
for i in range(len(p1)):
    for j in p1[i]:
        p.append(int(j))

x=100

start = timer()
print("Maksimum kar:",dynamicProgramming(m, p, x))
end = timer()
print((end - start)*1000000)

##

m1 = csv_to_list("Dist_yuz.csv")#100 değeri için çalışır
m = []
sum = 0
for i in range(len(m1)):
    for j in m1[i]:
        sum += int(j)
        m.append(sum)


p1 = csv_to_list("Kar_yuz.csv")
p = []
for i in range(len(p1)):
    for j in p1[i]:
        p.append(int(j))

x=100

start = timer()
print("Maksimum kar:",dynamicProgramming(m, p, x))
end = timer()
print((end - start)*1000000)

##

m1 = csv_to_list("Dist_bin.csv")#1000 değeri için çalışır
m = []
sum = 0
for i in range(len(m1)):
    for j in m1[i]:
        sum += int(j)
        m.append(sum)


p1 = csv_to_list("Kar_bin.csv")
p = []
for i in range(len(p1)):
    for j in p1[i]:
        p.append(int(j))

x=100

start = timer()
print("Maksimum kar:",dynamicProgramming(m, p, x))
end = timer()
print((end - start)*1000000)

##

m1 = csv_to_list("Dist_yuzbin.csv")#100000 değeri için çalışır
m = []
sum = 0
for i in range(len(m1)):
    for j in m1[i]:
        sum += int(j)
        m.append(sum)


p1 = csv_to_list("Kar_yuzbin.csv")
p = []
for i in range(len(p1)):
    for j in p1[i]:
        p.append(int(j))

x=100

start = timer()
print("Maksimum kar:",dynamicProgramming(m, p, x))
end = timer()
print((end - start)*1000000)


##

m1 = csv_to_list("Dist_birmilyon.csv")#1000000 değeri için çalışır
m = []
sum = 0
for i in range(len(m1)):
    for j in m1[i]:
        sum += int(j)
        m.append(sum)


p1 = csv_to_list("Kar_birmilyon.csv")
p = []
for i in range(len(p1)):
    for j in p1[i]:
        p.append(int(j))

x=100

start = timer()
print("Maksimum kar:",dynamicProgramming(m, p, x))
end = timer()
print((end - start)*1000000)