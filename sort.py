def sort_word(word: str):
   word_list= word.lower().split(' ')
   n=len(word_list)
   for i in range(n-1):
      min_ind=i
      for j in range(i+1,n):
         if word_list[j]< word_list[min_ind]:
            min_ind=j 
      temp=word_list[i]
      word_list[i]=word_list[min_ind]
      word_list[min_ind]=temp  
   return  word_list


my_word="Hello this Is an Example"
print(sort_word(my_word))