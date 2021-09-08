def computepay(h,r):
    if (h>40.0):
        t=h*r
        s=(h-40.0)*(r*0.5)
        cgp=t-s
    else:
        cgp=h*r
    return cgp
    # value of cgp goes into computepay (return function)

hrs = input("Enter Hours:")
h=float(hrs)
rph=input("Enter rate per hour:")
r=float(rph)
p = computepay(h,r)
print("Pay", p)