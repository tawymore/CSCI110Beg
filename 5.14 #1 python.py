def day_of_week (day_number):
     if day_number == 0:
         print ('sunday')
     elif day_number == 1:
          print ('Monday')
     elif day_number == 2:
          print ('Tuesday')
     elif day_number == 3:
          print ('Wednesday')
     elif day_number == 4:
          print ('Thursday')
     elif day_number == 5:
          print ('Friday')
     elif day_number == 6:
          print ('Saturday')
     else:
          print('Error, give me a number between 0 and 6')
          day_of_week (3)