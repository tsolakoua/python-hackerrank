def average(array):
    my_set = set(array)
    leng = len(my_set)
    return sum(my_set)/leng
  
if __name__ == '__main__':
   n = int(input())
   arr = list(map(int, input().split()))
   result = average(arr)
   print(result)
