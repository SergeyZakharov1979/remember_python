s1, s2, s3 = input(), input(), input()
short, long = s1, s1

if len(s2) < len(s1):
    short = s2
else:
    long = s2
if len(s3) < len(s2) and len(s3) < len(s1):
    short = s3
elif len(s3) > len(s2) and len(s3) > len(s1):
    long = s3

print( short, long, sep='\n')
