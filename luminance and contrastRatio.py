#the red green blue as parameters
def luminance(r,g,b):
#covert values to 0-1 scale
    ro=r/255
    go=g/255
    bo=b/255
#calculating new values based on the rule for Red
    if ro<=0.03928:
        ri=ro/12.92
    else:
        ri=((ro+0.055)/1.055)**2.4
#calculating new values based on the rule for Green
    if go<=0.03928:
        gi=go/12.92
    else:
        gi=((go+0.055)/1.055)**2.4
#calculating new values based on the rule for Blue
    if bo<=0.03928:
        bi=bo/12.92
    else:
        bi=((bo+0.055)/1.055)**2.4
#calculating luminance value of the color
    L=(0.2126*ri)+(0.7152*gi)+(0.0722*bi)
    return L


#calculating contrast ratio pf two colors
#rgb for both colors as parameters
def contrastRatio(r1,g1,b1,r2,g2,b2):
#calculte the luminance of  both colors by calling luminance function
    L1=luminance(r1,g1,b1)
    L2=luminance(r2,g2,b2)
    print("Luminance of color_1 =",round(L1*100,2),"%")
    print("Luminance of color_2 =",round(L2*100,2),"%")
#identify and assign the lighter and darker colors using luminance value
    if L1>L2:
        L_light=L1
        L_dark=L2
    else:
        L_light=L2
        L_dark=L1
#calculate contrast ratio
    Ck=round((L_light+0.05)/(L_dark+0.05),2)
    print("Contrast ration of the two colors is:",Ck)
contrastRatio(255,255,255,0,0,0)
