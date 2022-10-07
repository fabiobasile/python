hrs = 0; 
mins = 6; 
sec = 15; 
framecnt = 1200; 
import datetime;
etastring = (datetime.datetime.now() + (datetime.timedelta(hours=hrs, minutes=mins, seconds=sec)*framecnt)); 
print(etastring.strftime("Current rendering is estimated to complete on %A, %B %d %Y, at %I:%M:%S %p"));
