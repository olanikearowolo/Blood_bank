import sqlite3

conn =sqlite3.connect("BBMSDB.db")
cursor =conn.cursor()

cursor.execute('Drop table if exists LOGIN')
stmt ='create table LOGIN (username varchar(20),password int(4))'
cursor.execute(stmt)


#cursor.execute('Drop table if exists DONOR_INFO')
#stmt ='create table DONOR_INFO (donor_ID int(5),primary key, donor_name varchar(20),Address varchar(50),sex varchar(7),Email varchar(20),blood_group varchar(5),DOB date,contact_No int(12))'
#cursor.execute(stmt)

#cursor.execute('Drop table if exists APPOINTMENT_INFO')
#stmt='create table APPOINTMENT_INFO (patient_ID int(5),Appointment_NO int(5) primary key,Doctor_ID int(5),DOA date,Description varchar(50),Appoint_time time,Foreign key (patient_ID) refrences PATIENT_INFO(patient_ID)'
#cursor.execute(stmt)

#cursor.execute('Drop table if exists ROOM')
#stmt='create table ROOM (patient_ID int (5),ROOM_NO int(5) primary key,ROOM_type int(5),ROOM_charges int(5),Admitted date,Dischsrged date,Foreign key(patient_ID)references PATIENT_INFO(patient_ID)'
#cursor.execute(stmt)

#cursor.execute('Drop table if exists PATIENT_RECORD')
#stmt ='create table PATIENT_RECORD(patient_ID int(5) primary key,patient_name varchar(20)Medication varchar(50),illness varchar (40),operation varchar(20),operation_date date,operation_time time,foreign key(patient_ID)refrences PATIENT_INFO(patient_ID))'
#cursor.execute(stmt)



conn.commit()

cursor.close()
conn.close()
