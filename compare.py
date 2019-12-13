import sys

def versionCompare(v1, v2): 
      
    # Breakdown by version major, minor, and revision number 
    ver1 = v1.split(".") 
    ver2 = v2.split(".") 
  
    # Initiator  
    i = 0 
      
    while(i < len(ver1)): 
          
        # Version 2 is higher 
        if int(ver2[i]) > int(ver1[i]): 
            return -1
          
        # Version 1 is higher 
        if int(ver1[i]) > int(ver2[i]): 
            return 1
  
        # If undetermined  
        i += 1
          
    # Both the versions are equal 
    return 0
  
# Take the two command line arguments and compare them.  

version1 = (sys.argv[1])
version2 = (sys.argv[2])
  
ans =  versionCompare(version1, version2) 
if ans > 0: 
    print version1 + " is higher than " + version2
elif ans < 0: 
    print version2 + " is higher than " + version1
else: 
    print version1 + "is the same as " + version2
  

