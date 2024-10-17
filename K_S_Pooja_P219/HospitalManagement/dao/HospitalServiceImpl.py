import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dao.IHospitalService import IHospitalService
from entity.appointment import Appointment
from exception.PatientNumberNotFound import PatientNumberNotFoundException
from util.DBConnection import DBConnection
from  tabulate import tabulate

class HospitalServiceImpl(IHospitalService):

    def getAppointmentById(self, appointmentId):
        conn = DBConnection.get_connection()
        cursor=conn.cursor()
        try:
            query = "SELECT * FROM Appointment WHERE appointmentId = ?"
            cursor.execute(query, (appointmentId,))
            appointment = cursor.fetchone()

            if appointment:
                appointment_details=[
                    ['Appointment ID',appointment[0]],
                    ["Patient ID",appointment[1]],
                    ["Doctor ID",appointment[2]],
                    ["Appointment Date",appointment[3]],
                    ["Description",appointment[4]],
                ]
                print("-----------Appointment Details---------- ")
                print(tabulate(appointment_details,tablefmt="grid"))

            else:
                print("------------Appointment Not Found----------")
        except Exception as e:
            print(f"Error in fetching appointment: {e}")
            return None
        finally:
            cursor.close()


    def getAppointmentsForPatient(self, patientId):
        conn = DBConnection.get_connection()
        cursor=conn.cursor()
        try:
            query = "SELECT * FROM Appointment WHERE patientId = ?"
            cursor.execute(query,(patientId,))
            appointments = []
            for row in cursor.fetchall():
                appointments.append(Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    doctorId=row[2],
                    appointmentDate=row[3],
                    description=row[4]
                ))

            return appointments
        except PatientNumberNotFoundException as e:
            print(e)
            return []
        finally:
            cursor.close()



    def getAppointmentsForDoctor(self, doctorId):
        conn = DBConnection.get_connection()
        cursor=conn.cursor()
        try:
            query = "SELECT * FROM Appointment WHERE doctorId = ?"
            cursor.execute(query, (doctorId,))
            appointments = []
            for row in cursor.fetchall():
                appointments.append(Appointment(
                    appointmentId=row[0],
                    patientId=row[1],
                    doctorId=row[2],
                    appointmentDate=row[3],
                    description=row[4]

                ))
            return appointments
        except Exception as e:
            print(f"Error in fetching appointments for doctor: {e}")
            return []
    def doctor_exists(self, doctorId):
        conn = DBConnection.get_connection()
        cursor=conn.cursor()
        try:
            query = "SELECT count(*) FROM Doctor WHERE doctorId = ?"
            cursor.execute(query, (doctorId,))
            count = cursor.fetchone()[0]
            return count > 0 #If doctor exists
        except Exception as e:
            print(f"Error in doctor exists: {e}")
            return False
        finally:
            cursor.close()
    def patient_exists(self, patientId):
        conn = DBConnection.get_connection()
        cursor=conn.cursor()
        try:
            query = "SELECT count(*) FROM Patient WHERE patientId = ?"
            cursor.execute(query, (patientId,))
            count = cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print(f"Error in patient exists: {e}")
            return False
        finally:
            cursor.close()
    def get_next_appointmentId(self):
        conn = DBConnection.get_connection()
        cursor=conn.cursor()
        try:
            cursor.execute("SELECT Max(appointmentId) FROM Appointment")
            max_id = cursor.fetchone()[0]
            return (max_id+1) if max_id is not None else 1
        except Exception as e:
            print(f"Error in get_next_appointment: {e}")
            return 1
        finally:
            cursor.close()

    def scheduleAppointment(self, appointment):
        conn = DBConnection.get_connection()
        cursor=conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM Patient where patientId=?",(appointment.get_patientId(),))
            patient_exists = cursor.fetchone()[0]
            if not patient_exists:
                print(f"Patient ID {appointment.get_patientId()} does not exist")
                return False

            cursor.execute("Select Count(*) From Doctor where doctorId=?",(appointment.get_doctorId(),))
            doctor_exists = cursor.fetchone()[0]
            if not doctor_exists:
                print(f"Doctor ID {appointment.get_doctorId()} does not exist")
                return False

            cursor.execute("INSERT INTO Appointment (appointmentId, patientid, doctorId, appointmentDate, description) VALUES (?,?,?,?,?)",
            (appointment.get_appointmentId(),appointment.get_patientId(), appointment.get_doctorId(), appointment.get_appointmentDate(), appointment.get_description()))
            conn.commit()
            print("Appointment Scheduled")
            return True
        except Exception as e:
            print(f"Error in scheduleAppointment: {e}")


    def updateAppointment(self, appointment):
        conn = DBConnection.get_connection()
        cursor=conn.cursor()
        try:
            cursor.execute("Select count(*) from Appointment where appointmentId=?",(appointment.appointmentId,))
            count = cursor.fetchone()[0]
            if not count:
                print("---------Appointment Not Found----------")
                return False

            cursor.execute("UPDATE Appointment SET patientId=?,doctorId=?, appointmentDate = ?, description = ? WHERE appointmentId = ?",(appointment.get_patientId(),appointment.get_doctorId(),appointment.get_appointmentDate(),appointment.get_description(),appointment.appointmentId))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error in updateAppointment: {e}")
            return False
        finally:
            cursor.close()

    def cancelAppointment(self, appointmentId):
        conn = DBConnection.get_connection()
        cursor=conn.cursor()
        try:
            cursor.execute("Select count(*) from Appointment where appointmentId=?",(appointmentId,))
            count = cursor.fetchone()[0]
            if count==0:
                print("---------Appointment Not Found----------")
                return False

            cursor.execute("DELETE FROM Appointment WHERE appointmentId = ?",(appointmentId,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error in cancelAppointment: {e}")
            return False
        finally:
            cursor.close()

