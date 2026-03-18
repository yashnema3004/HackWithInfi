# def find_superstar_dish(arr,n):
#     arr.sort()
#     i = 0
#     res = []
#     while i < n:
#         count = 1
#         j = i+1
        
#         while j < n and arr[i] == arr[j]:
#             count +=1
#             j +=1
            
#             if count > n//3:
#                 res.append(arr[i])
                
#         i = j
#     if not res:
#         return "-1"
            
#     return " ".join(map(str,res))
                


# new_arr = [2,2,1,1,1,2]
# n = 6
# print(find_superstar_dish(new_arr,n)) 

# def find_superstar_dish(arr , n):
#     count1 , count2 = 0 , 0
#     candidate1 , candidate2 = None , None    
#     for num in arr:
#         if num == candidate1:
#             count1 +=1
#         elif num == candidate2:
#             count2 +=1
#         elif count1 == 0:
#             candidate1 = num
#             count1 = 1
#         elif count2 == 0:
#             candidate2 = num
#             count2 = 1
#         else:
#             count1 -=1
#             count2 -=1
        
#     res = []
#     count1 , count2 = 0 , 0
    
#     for num in arr:
#         if num == candidate1:
#             count1 +=1
#         elif num == candidate2:
#             count2 +=1
        
#     if count1 > n//3:
#         res.append(candidate1)
#     if count2 > n//3:
#         res.append(candidate2)
        
#     return " ".join(map(str , res))

# new_arr = [1,2,2,2,1,1]
# n = 6

# print(find_superstar_dish(new_arr,n))


