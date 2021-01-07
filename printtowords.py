# given the time in numeral and convert it into words  
 
  
# print time in words. 

def printWords(hours, minutes): 
    nums = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", 
            "fourteen", "fifteen", "sixteen",  
            "seventeen", "eighteen", "nineteen",  
            "twenty", "twenty one", "twenty two",  
            "twenty three", "twenty four",  
            "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine"]
  
    if (minutes == 0): 
        print(nums[hours], "o' clock")
  
    elif (minutes == 1): 
        print("one minute past", nums[hours]) 
  
    elif (minutes == 59): 
        print("one minute to", nums[(hours % 12) + 1]) 
  
    elif (minutes == 15): 
        print("quarter past", nums[hours]) 
  
    elif (minutes == 30): 
        print("half past", nums[hours])
  
    elif (minutes == 45): 
        print("quarter to", (nums[(hours % 12) + 1]))
  
    elif (minutes <= 30): 
        print(nums[minutes],"minutes past", nums[hours]) 
  
    elif (minutes > 30): 
        print(nums[60 - minutes], "minutes to",  
              nums[(hours % 12) + 1]) 


hours = 5; 
minutes = 1; 
  
printWords(hours, minutes); 