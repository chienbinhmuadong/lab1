a=0
with open("D:/nam nhat/term1/Programming/lab1/books.csv", "r", encoding="cp1251", errors="ignore") as file:
     for line in file:
          if len(line)>2:
            a+=1
print("количество записей в файле: ",a)