from __future__ import division

##hackerrank python intro Whats your Name
#this is a nice little formatting question, see below
first=raw_input('Enter first name: ')
last=raw_input('Enter last name: ')
print'Hello {0} {1}! You just delved into python.'.format(first,last)


##hackerrank python intro Triangle Quest
for i in range(1,9):    
    print int(i*pow(10,i-1) + i*pow(10,i-2) + i*pow(10,i-3) + i*pow(10,i-4) 
    + i*pow(10,i-5) + i*pow(10,i-6) + i*pow(10,i-7) + i*pow(10,i-8) + i*pow(10,i-9))


##hackerrank python intro Interchange two Numbers
a=int(raw_input('Entere a here: '))
b=int(raw_input('Enter b here: '))
ans=(a,b)
print ans[1]
print ans[0]

##hackerrank python intro Finding the percentage
# the trick for this problem (for me) was understanding the output format
# it is also important to note that this method allows the dict to append values
# note this requires from__future__ import division

N=int(raw_input('Enter N here: '))
ans={}
for i in range(0,N):
    a = raw_input('Enter names here: ')
    a = a.split()
    ans[a[0]]= sum([float(n) for n in a[1:]])/len(a[1:])
    print ans

print ans
b = raw_input('For whom should I find the avg grade? ')
print '{:.2f}'.format(ans[b])


# the format method is needed to print the output in the desired format
# the old way to accomplish this is: 
print '%.2f' % ans[b]

# the more recent method of formatting is described here:
# http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/float.html
# https://docs.python.org/2/library/string.html#formatspec
print '{:.2f}'.format(ans[b])