def greet(givenName, familyName = ""):

    if familyName == "":
        print ("Hi " + givenName + ". It is a pleasure to meet you.")    

    else:
        print ("Hi there, " + givenName +  " of " + familyName + ". It is a pleasure to meet you.")


name = "Eduard"
familyN = "Ruiz"

greet(name, familyN)
