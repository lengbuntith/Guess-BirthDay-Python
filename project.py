#Take user type main() to start program
print("To Start Please Type: main()")
def main():
  print(" CALCULATE YOUR DATE OF BIRTH")
  string="******************************"
  print(string)
  #take user inpu
  date=int(input("Enter date : "))         
  month=int(input("Enter month : "))
  year=int(input("Enter year : "))
  if date in [29,30,31]:
    if month ==2:
      if year%4==0:
        main()
  i=1
  while (i>=2):
    try:
      date=int(input("Enter date : "))
    except:
      date=int(input("Enter date again : "))
  #if 29.02.in any year is divided to 4  
  #[1900-1999->codeofyear=(x/4 +x+1)%7
  #[2000-2100->codeofyear=(x/4 +x)%7
  if year >= 1900:
    x=(year-1900)
    codeofyear=(x//4+x+1)%7
  if year >= 2000:
    x=(year-2000)
    codeofyear=(x//4+x)%7
  #We calculate just for year in (1900-2100)
  if year <= 1900:
    print(string)
    print("      Please Enter Again")
    print(string,"\n")
    main()
  if year >= 2100:
    print(string)
    print("      Please Enter Again")
    print(string,"\n")
    main()
  #For year is divided to 4 -> codeofjan=5 and codeoffeb=1
  if year%4==0:
    codeofjan=5
    codeoffeb=1
  else:
    codeofjan=6
    codeoffeb=2
  
  if month == 1:daycode=(date+codeofjan+codeofyear)%7 
  if month == 2:daycode=(date+codeoffeb+codeofyear)%7
  if month == 3:daycode=(date+2+codeofyear)%7
  if month == 4:daycode=(date+5+codeofyear)%7
  if month == 5:daycode=(date+0+codeofyear)%7
  if month == 6:daycode=(date+3+codeofyear)%7
  if month == 7:daycode=(date+5+codeofyear)%7
  if month == 8:daycode=(date+1+codeofyear)%7
  if month == 9:daycode=(date+4+codeofyear)%7
  if month == 10:daycode=(date+6+codeofyear)%7
  if month == 11:daycode=(date+2+codeofyear)%7
  if month == 12:daycode=(date+4+codeofyear)%7
  print(string)
  
  day=["Sunday","Monday","Tuesdday","Wednesday","Thurday","Friday","Saturday","Sunday"]
  print("     You born on",day[daycode],"    ")
  print(string)

  start=input("1.Start Again\n2.Exit\nEnter Number : ")
  if start == '1':
    print("\n")
    main()
  elif start == '2':
    exit()
  else:
    print(string)
    print("      Please enter again")
    print(string,"\n")
    main()
