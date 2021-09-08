score = input("Enter Score: ")
try:
    s=float(score)
    if (0.0<=s<=1.0):
        if s>=0.9:
            print('A')
        elif (0.9>s>=0.8):
            print('B')
        elif (0.8>s>=0.7):
            print('C')
        elif (0.7>s>=0.6):
            print('D')
        elif (s<0.6):
            print('F')
    else:
        print('Score is out of range')
except:
    print("Error, Kindly enter a floating data type ")
    quit()