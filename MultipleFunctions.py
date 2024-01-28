lists = ["Machine Learning", "Neural networks", "Vision", "Robotics", "Speech Processing", "Natural Language processing"]
class MultipleFunctions():
    def Subfields():
        lists = ["Machine Learning", "Neural networks", "Vision", "Robotics", "Speech Processing", "Natural Language processing"]
        print("Sub-fields in AI are:")
        for x in lists:
            print(x)
            
    def oddEven():
        num = int(input("Enter a number: "))
        if(num%2==1):
            print(num, "is odd number")
        else:
            print(num, "is even number")
            
    def Elegible():
        Gender = input("Your Gender: ")
        Age = int(input("Your Age: "))
        if(Gender=="Male"):
            if(Age>21):
                print("Elegible")
            else:
                print("Not elegible")
        else:
            if(Age>18):
                print("Elegible")
            else:
                print("Not elegible")
                
    def percentage():
        Subject1= int(input("Subject1= "))
        Subject2= int(input("Subject2= "))
        Subject3= int(input("Subject3= "))
        Subject4= int(input("Subject4= "))
        Subject5= int(input("Subject5= "))
        total = Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total : ",total)
        Percentage = (total/500)*100
        print("percentage : ",Percentage)
        
    def triangle():
        Height=int(input("Height: "))
        Breadth=int(input("Breadth: "))
        print("Area formula : (Height*Breadth)/2")
        Area_of_Triangle = (Height*Breadth)/2
        print("Area of Triangle: ", Area_of_Triangle)
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))   
        Breadth=int(input("Breadth: "))
        print("Perimeter formula : Height1+Height2+Breadth")
        Perimeter_of_triangle=Height1+Height2+Breadth
        print("Perimeter of Triangle:", Perimeter_of_triangle)