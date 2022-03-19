import rolls_w_name
import rolls_w_reg
import time




DBroll = []

# function for animation 
def check_anime():
  list = 'Checking'
  i = 0

  while i < 7:
    list += "."
    i += 1
    time.sleep(0.2)
    print(list,  end="\r")



global roll
#Making function for 1st choice
def ColCh1():
  i_choice= input("Enter the College EIIN:")
  i_shift= input("Enter your Shift:")
  i_Group= input("Enter your Group:")
  global Choice_i
  Choice_i=["1st Choice"]
  Choice_i.append(i_choice)
  Choice_i.append(i_shift)
  Choice_i.append(i_Group)
  
  
#Making function for 2nd choice
def ColCh2():
  ii_choice= input("Enter the College EIIN:")
  ii_shift= input("Enter your Shift:")
  ii_Group= input("Enter your Group:")
  global Choice_ii
  Choice_ii=["2nd Choice"]
  Choice_ii.append(ii_choice)
  Choice_ii.append(ii_shift)
  Choice_ii.append(ii_Group)
  
  
#Making function for 3rd choice 
def ColCh3():
  iii_choice= input("Enter the College EIIN:")
  iii_shift= input("Enter your Shift:")
  iii_Group= input("Enter your Group:")
  global Choice_iii
  Choice_iii=["3rd Choice"]
  Choice_iii.append(iii_choice)
  Choice_iii.append(iii_shift)
  Choice_iii.append(iii_Group)


#roll cheking function 
def CheckRoll():
  if roll in rolls_w_name.rwname:
    if reg_no== rolls_w_reg.rwreg[roll]:
      check_anime()
      
      print("               ")
      print("Hello", rolls_w_name.rwname[roll], ", Please proceed with your choice in your Dream Colleges.")
      TakeChoice()
    else:
      check_anime()
      
      print("               ")
      print("Sorry, your Roll & Registration Number doesn't match. Please try with your Real details")
      GetRoll()
      CheckRoll()
    
  else:
    check_anime()
      
    print("               ")
    print("Plz Enter a Valid Roll Number")
    GetRoll()
    CheckRoll()

#function for get roll & reg number
def GetRoll():
  global roll
  global reg_no

  roll = int(input("What's your Roll:"))
  reg_no = int(input("What's your Registration Number:"))


#function for recap choice
def printchoices():  
  print("               ")
  print("Hey",rolls_w_name.rwname[roll], ", Here is a quick recap of your Choice.")

  print(Choice_i)
  print(Choice_ii)
  print(Choice_iii)


# Take choice from student 
def TakeChoice():
  ColCh1()
  ColCh2()
  ColCh3()
  printchoices()

def Groll():

  GetRoll()
  CheckRoll()
  DBroll.append(roll)

  


#Calling my function for run
Groll()

print("Designed & Developed By Fahad Dhruba.")