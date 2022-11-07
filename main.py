class Student:
    def __init__(self, name, ID, favColor, next=None):
        self.name = name
        self.ID = ID
        self.favColor = favColor
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, name, ID, favColor):
        newStudent = Student(name, ID, favColor) #insantiate a new student mode
        if self.head: #check if a head exists
            current = self.head #create a temporary pointer to the head node
            #while there's another node in the line, "walk" down the line until the end
            while current.next:
                current = current.next 
            current.next = newStudent #add the new student to the end
        else:
            self.head = newStudent #if there was no head student, insert at front of empty line
    
    def printList(self):
        current = self.head
        while current:
            print("Student name:", current.name, ", ID:", current.ID," favorite color: ", current.favColor)
            current = current.next
        
#----------------------------------------------
StudentLine = LinkedList()
StudentLine.insert("Lily", 456987, "white")
StudentLine.insert("Kevin", 123987, "white")
StudentLine.insert("Sebastian", 4, "white")
StudentLine.insert("Ricky", 7844, "yellow")
StudentLine.insert("Lukas", 4832, "blue")
StudentLine.insert("Dom", 90430, "blue")
StudentLine.printList()
