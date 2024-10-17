import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dao.HospitalServiceImpl import HospitalServiceImpl
from entity.appointment import Appointment
from tabulate import tabulate

class MainModule:
    def __init__(self):
        self.hospital_service = HospitalServiceImpl()

    def menu(self):
        global appointment
        print("*" * 40)
        print("Welcome to Hospital Management System")
        print("*" * 40)
        while True:
            menu = [
                ["1.", "Get Appointment Details by ID"],
                ["2.", "Get Appointments for Patient"],
                ["3.", "Get Appointments for Doctor"],
                ["4.", "Schedule Appointment"],
                ["5.", "Update Appointment"],
                ["6.", "Cancel Appointment"],
                ["7.", "Exit"]
            ]
            # Print the menu using tabulate
            print(tabulate(menu, headers=["Option", "Description"], tablefmt="grid"))


            choice = input("Enter your choice: ")

            if choice == '1':
                appointment_id=int(input("Enter Appointment ID: "))
                try:
                    appointment=self.hospital_service.getAppointmentById(appointment_id)
                    if appointment is None:
                        print("")
                except ValueError :
                    print("Invalid input. Please enter a valid number.")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == '2':
                patient_id=input("Enter Patient ID to fetch appointment: ")
                appointments=self.hospital_service.getAppointmentsForPatient(patient_id)
                if appointments:
                    print(f"Appointments for Patient: {patient_id}")
                    table_data = [[appointment.appointmentId, appointment.doctorId, appointment.appointmentDate,
                                   appointment.description]
                                  for appointment in appointments]
                    headers = ["Appointment Id", "Doctor Id","Appointment Date", "Appointment Description"]
                    print(tabulate(table_data, headers=headers,tablefmt="grid"))
                else :
                    print("Patient not found")


            elif choice == '3':
                doctor_id=input("Enter Doctor ID to fetch appointments: ")
                if not self.hospital_service.doctor_exists(doctor_id):
                    print(f"*****The doctor Id {doctor_id} doesnot exists******")
                    continue
                appointments=self.hospital_service.getAppointmentsForDoctor(doctor_id)
                if appointments:
                    print(f"Appointments for Doctor: {doctor_id}")
                    table_data = [[appointment.appointmentId, appointment.patientId, appointment.appointmentDate,
                                   appointment.description]
                                  for appointment in appointments]
                    headers=["Appointment Id", "Patient Id", "Appointment Date", "Appointment Description"]
                    print(tabulate(table_data, headers=headers,tablefmt="grid"))
                else:
                    print(f"--------No appointments for Doctor {doctor_id}--------")
            elif choice == '4':
                patient_id=input("Enter Patient Id: ")
                doctor_id=input("Enter Doctor ID: ")
                appointment_date=input("Enter Appointment Date(YYYY-MM-DD HH:MM): ")
                description=input("Enter Appointment Description: ")
                appointment_id=self.hospital_service.get_next_appointmentId()
                if appointment_id is None:
                    print("Failed to get next appointment.")
                else:
                    appointment = Appointment(
                        appointmentId=appointment_id,  # Use the generated ID
                        patientId=patient_id,
                        doctorId=doctor_id,
                        appointmentDate=appointment_date,
                        description=description
                    )
                if self.hospital_service.scheduleAppointment(appointment):
                    print("Appointment scheduled successfully.")
                else:
                    print("Unable to schedule appointment.")

            elif choice == '5':
                appointment_id=int(input("Enter Appointment ID to update: "))
                new_patient_id=input("Enter New Patient ID: ")
                if not self.hospital_service.patient_exists(new_patient_id):
                    print("The specified patient Id does not exist.")
                    continue
                new_doctor_id=input("Enter New Doctor ID: ")
                new_appointment_date=input("Enter New Appointment Date(YYYY-MM-DD HH:MM): ")
                new_description=input("Enter New Appointment Description: ")
                appointment=Appointment(
                    appointmentId=appointment_id,
                    patientId=new_patient_id,
                    doctorId=new_doctor_id,
                    appointmentDate=new_appointment_date,
                    description=new_description
                )
                if self.hospital_service.updateAppointment(appointment):
                    print("-------------Appointment updated successfully------------")
                else:
                    print("Unable to update appointment.")
            elif choice == '6':
                appointment_id=int(input("Enter Appointment ID to cancel: "))
                if self.hospital_service.cancelAppointment(appointment_id):
                    print("Appointment cancelled successfully.")
                else:
                    print("Appointment id does not exist")
            elif choice == '7':
                print("Existing the system")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.menu()