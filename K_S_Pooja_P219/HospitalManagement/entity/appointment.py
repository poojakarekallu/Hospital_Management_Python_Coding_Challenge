class Appointment:
    def __init__(self,appointmentId,patientId,doctorId,appointmentDate,description):
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentId = appointmentId
        self.appointmentDate = appointmentDate
        self.description = description

#Setter methods

    def set_appointmentId(self,appointmentId):
        self.appointmentId = appointmentId
    def set_patientId(self,patientId):
        self.patientId = patientId
    def set_doctorId(self,doctorId):
        self.doctorId = doctorId
    def set_appointmentDate(self,appointmentDate):
        self.appointmentDate = appointmentDate
    def set_description(self,description):
        self.description = description

    #Getter methods

    def get_appointmentId(self):
        return self.appointmentId
    def get_patientId(self):
        return self.patientId
    def get_doctorId(self):
        return self.doctorId
    def get_appointmentDate(self):
        return self.appointmentDate
    def get_description(self):
        return self.description

    def __str__(self):
        return f"Appointment ID: {self.appointmentId}, Patient ID: {self.patientId}, Doctor ID: {self.doctorId}, " \
               f"Date: {self.appointmentDate}, Description: {self.description}"