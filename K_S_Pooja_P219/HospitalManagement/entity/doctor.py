class Doctor:
    def __init__(self,doctorId,firstName,lastName,specialization,contactNumber):
        self.doctorId = doctorId
        self.firstName = firstName
        self.lastName = lastName
        self.specialization = specialization
        self.contactNumber = contactNumber

    #Setter methods

    def set_doctorId(self,doctorId):
        self.doctorId = doctorId
    def set_firstName(self,firstName):
        self.firstName = firstName
    def set_lastName(self,lastName):
        self.lastName = lastName
    def set_specialization(self,specialization):
        self.specialization = specialization
    def set_contactNumber(self,contactNumber):
        self.contactNumber = contactNumber

    #Getter methods

    def get_doctorId(self):
        return self.doctorId
    def get_firstName(self):
        return self.firstName
    def get_lastName(self):
        return self.lastName
    def get_specialization(self):
        return self.specialization
    def get_contactNumber(self):
        return self.contactNumber

    def __str__(self):
        return f"Doctor ID: {self.doctorId}, Name: {self.firstName} {self.lastName}, " \
               f"Specialization: {self.specialization}, Contact: {self.contactNumber}"