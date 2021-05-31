"""
Müslüm Türk
Program that finds the base station combination that gives the maximum profit with Greedy algorithm
"""
import csv
from timeit import default_timer as timer

def greedy(m, p, x):
    n = len(m)
    lis = []
    
    for i in range(0,n):
        lis.append(p[i]/(m[i]))

    for i in range(n):
        for j in range(i+1, n):
            if lis[j]>lis[i]:
                temp = lis[i]
                lis[i] = lis[j]
                lis[j] = temp
                temp = m[i]
                m[i] = m[j]
                m[j] = temp
                temp = p[i]
                p[i] = p[j]
                p[j] = temp
    
    print(m)
    stations = []
    flag = 0
    ans=0
    for i in range(n):
        for j in range(len(stations)):
            if not (m[i]-stations[j] >= x or stations[j]-m[i] >= x):
                flag = 1
        if flag != 1:
            ans += p[i]
            stations.append(m[i])
        flag = 0
            
    stations.sort()
    print("İstasyonların merkeze uzaklıkları:", stations)
    return ans



def csv_to_list(filename):#csv dosyalarını okumak için
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)


######################################################################################

m1 = csv_to_list("Dist_on.csv") #10 değeri için çalışır
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
print("Maksimum kar:",greedy(m, p, x))
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
print("Maksimum kar:",greedy(m, p, x))
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
print("Maksimum kar:",greedy(m, p, x))
end = timer()
print((end - start)*1000000)

