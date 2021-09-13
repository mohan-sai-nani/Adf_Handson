create table REQUEST_INFO (
						   ID int not null auto_increment primary key,
						   FIRST_NAME varchar(20) not null,
						   MIDDLE_NAME varchar(20),
						   LAST_NAME varchar(20) not null,
						   DOB date not null,
						   GENDER varchar(1) not null constraint ck_gender check (GENDER in ('M', 'F')),
						   NATIONALITY varchar(20) not null,
						   CURRENT_CITY varchar(20) not null,
						   STATE varchar(20) not null,
						   PIN_CODE int not null,
						   QUALIFICATION varchar(20) not null,
						   SALARY int not null,
						   PAN_NUMBER varchar(20) not null,
                           REQUEST_DATE DATETIME not null default NOW()
						   );