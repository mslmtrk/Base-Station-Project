"""
Müslüm Türk
Program that finds the base station combination that gives the maximum profit with Brute Force algorithm
"""
import csv
from timeit import default_timer as timer

def listEndHere(m, p, x, curr):
    max_local = p[curr]
    if(curr == 0):#base case
        return p[0]
    last = 0

    for i in range(curr-1, -1, -1):#baştan curr indeksine kadar olan tüm kombinasyonlar karşılaştırılır
        if(m[curr]-m[i] >= x):
            a = p[curr] + listEndHere(m, p, x, i)
            if(a >= max_local):
                max_local = a
                last = i

    stations[last] = 1         
    return max_local;#curr indeksine kadar olan max kombinasyon

def bruteForce(m, p, x): 
    n = len(m)
    max_ans = p[0]
    global stations #seçilen istasyonları yazdırmaya yarar

    stations = []
    for i in range(n):
        stations.append(0)

    for i in range(n):#Her bir indeks kombine edilecek listenin son indeksi olarak düşünülür
        for j in range(n):
            stations[j] = 0
        stations[i] = 1
        a = listEndHere(m, p, x, i)
        if(a >= max_ans):#en büyük local maxı ve seçilen istasyonları alır 
            max_ans = a
            stations_ans = stations.copy()

    ls = []
    for i in range(n):#Seçilen istasyonların mesafeleri yazdırılır
        if stations_ans[i] == 1:
            ls.append(m[i])
    print("İstasyonların merkeze uzaklıkları:", ls)
    
    return max_ans

def csv_to_list(filename):#csv dosyası okunur
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
print("Maksimum kar:",bruteForce(m, p, x))
end = timer()
print("Time:",(end - start)*1000000,"ms")