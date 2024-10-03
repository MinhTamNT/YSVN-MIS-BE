import pyodbc

from ysvnmis import get_connection


def insert_data(job_title, start_time, end_time, priority, content, with_person, transportation_mode, next_appointment, referral, cost, notes, attachment_url, status):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            sql = """
            INSERT INTO [YSVNMIS].[dbo].[Collaborate] 
                ([JobTitle], [StartTime], [EndTime], [Priority], [Content], [WithPerson], [TransportationMode], [NextAppointment], [Referral], [Cost], [Notes], [AttachmentURL], [Status]) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (job_title, start_time, end_time, priority, content, with_person, transportation_mode, next_appointment, referral, cost, notes, attachment_url, status))
            connection.commit()
            print("Data inserted successfully!")
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")


def get_all_data():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            sql = "SELECT * FROM Collaborate AS C ORDER BY C.StartTime ASC"
            cursor.execute(sql)
            rows = cursor.fetchall()

            result = []
            columns = [column[0] for column in cursor.description]
            for row in rows:
                result.append(dict(zip(columns, row)))
            return result
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
            return None
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")
        return None


def update_data(id, job_title, start_time, end_time, priority, content, with_person, transportation_mode, next_appointment, referral, cost, notes, attachment_url, status):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            sql = """
            UPDATE [YSVNMIS].[dbo].[Collaborate]
            SET 
                [JobTitle] = ?, 
                [StartTime] = ?, 
                [EndTime] = ?, 
                [Priority] = ?, 
                [Content] = ?, 
                [WithPerson] = ?, 
                [TransportationMode] = ?, 
                [NextAppointment] = ?, 
                [Referral] = ?, 
                [Cost] = ?, 
                [Notes] = ?, 
                [AttachmentURL] = ?, 
                [Status] = ?
            WHERE [AutoID] = ?
            """
            cursor.execute(sql, (job_title, start_time, end_time, priority, content, with_person, transportation_mode, next_appointment, referral, cost, notes, attachment_url, status, id))
            connection.commit()
            print("Data updated successfully!")
        except pyodbc.Error as ex:
            print(f"Error: {ex}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("Failed to connect to the database.")

