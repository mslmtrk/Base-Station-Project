"""
Müslüm Türk
Program that finds the base station combination that gives the maximum profit with Divide and Conquer algorithm
"""
import csv
from timeit import default_timer as timer

def findIndex(stations, item, x):
    n = len(stations) - 1 
    low = 0
    high = n

    if n == 0:#eleman sayısı 1 ise
        if (stations[low] - item) >= x:#item başa yani 0. indexe eklenir
            return low
        elif (item - stations[low]) >= x:#item sona yani 1. indexe eklenir
            return -2
        else: #eklenmez
            return -1
    
    while low < high:#item'den büyük ilk index bulunur
        mid = (low + high)//2
        if(stations[mid] <= item):
            low = mid+1
        else:
            high = mid
    
    if low == 0:#ilk index'e gelindiyse
        if (stations[low] - item) >= x:#item başa yani 0. indexe eklenir
            return low
        else: #eklenmez
            return -1

    if low == n:#son index'e gelindiyse
        if (item - stations[low-1]) >= x and (stations[low] - item) >= x:#item sondan bir önceki indexe eklenir
            return low
        elif (item - stations[low]) >= x:#item son indexe eklenir
            return -2
        else: #eklenmez
            return -1

    if (item - stations[low-1]) >= x and (stations[low] - item ) >= x:#index'in iki yanında eleman vardır
        return low

    return -1

def myFunc(e):
    return e.p/e.m
            
def DivideAndConquer(m, p, x):
    n = len(m)
    lis = []
    class station:
        def __init__(self, m, p): 
            self.m = m
            self.p = p
    
    for i in range(n):#lis dizisine station türünde m ve p değerleri eklenir
        lis.append(station(m[i], p[i]))
    
    lis.sort(reverse=True, key=myFunc)# lis dizisi p/m oranına göre sıralanır
    
    stations = []
    stations.append(lis[0].m)
    ans = lis[0].p

    for i in range(1,n):#seçilen istasyonlar ve max kar bulunur
        index = findIndex(stations, lis[i].m, x)   
        if index == -2:
            stations.append(lis[i].m)
            ans += lis[i].p
        elif index != -1:
            stations.insert(index, lis[i].m)
            ans += lis[i].p
    
    print("İstasyonların merkeze uzaklıkları:", stations)
    return ans



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
print("Maksimum kar:",DivideAndConquer(m, p, x))
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
print("Maksimum kar:",DivideAndConquer(m, p, x))
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
print("Maksimum kar:",DivideAndConquer(m, p, x))
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
print("Maksimum kar:",DivideAndConquer(m, p, x))
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
print("Maksimum kar:",DivideAndConquer(m, p, x))
end = timer()
print((end - start)*1000000)