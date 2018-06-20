### Kebing Li
### Test file for pyRandomdotOrg, i.e. the random number collector from RANDOM.ORG 

import pyRandomdotOrg

if __name__ == '__main__':
    random = pyRandomdotOrg.clientlib("kebingli","kebingli@colby.edu")
    print "random generates integer list"
    print random.IntegerGeneratorList(3,1,10)
    print "random generates integer"
    print random.IntegerGenerator(1,100)
    print "generates a random desired string"
    print random.StringGenerator(3,3)
    print "generates a random string"
    print random.RandomString(5)
    

