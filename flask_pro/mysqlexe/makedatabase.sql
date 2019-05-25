create database childreading;
use childreading;
create table student_info(
	stu_id varchar(15),
	credit int, 
	qresult varchar(50), 
	rec_result varchar(25), 
	primary key(stu_id)
);

create table teacher_info(
	tea_id varchar(15),
	tea_email varchar(50),
	tea_name varchar(25), 
	password varchar(25), 
	teacher_intro varchar(255), 
	primary key(tea_id)
);

create table setcourse_info(
	scourse_id varchar(15), 
	scourse_title varchar(60),
	scourse_theme varchar(50),
	scourse_stage varchar(50),
	pageimg_urls varchar(255), 
	scourse_intro varchar(255),
	buylink varchar(255), 
	scourse_credit int, 
	scourse_price demical(10,2),
	primary key(scourse_id)
);

create table percourse_info(
	pcourse_id varchar(15), 
	vedio_url varchar(255), 
	pcourse_intro text,
	pcourse_pageimgurl varchar(255),
	primary key(pcourse_id)
);


create table s_p_class_info(
	id varchar(15),
	scourse_id varchar(15),
	pcourse_id varchar(15),
	thenumber int(2),
	primary key(id),
	foreign key(scourse_id) references setcourse_info(scourse_id) on delete cascade on update cascade,
	foreign key(pcourse_id) references percourse_info(pcourse_id) on delete cascade on update cascade
);


create table problems(
	pro_id varchar(15),
	pro_stem text,
	choice text,
	answer char(1),
	flag int,
	scourse_id varchar(15),
	pcourse_id varchar(15),
	pro_num varchar(15),
	primary key(pro_id),
	foreign key(scourse_id) references setcourse_info(scourse_id) on delete cascade on update cascade,
	foreign key(pcourse_id) references percourse_info(pcourse_id) on delete cascade on update cascade
);

create table class_info(
	class_id varchar(15),
	tea_id varchar(15),
	scourse_id varchar(15),
	start_time date,
	end_time date,
	primary key(class_id),
	foreign key(tea_id) references teacher_info(tea_id) on delete cascade on update cascade,
	foreign key(scourse_id) references setcourse_info(scourse_id) on delete cascade on update cascade
);


create table takes_table(
	stu_id varchar(15),
	scourse_id varchar(15),
	stage int,
	foreign key(scourse_id) references setcourse_info(scourse_id) on delete cascade on update cascade,
	foreign key(stu_id) references student_info(stu_id) on delete cascade on update cascade
);
  
create table inclass(
  stu_id varchar (15),
  class_id varchar (15),
  foreign key(stu_id) references student_info(stu_id) on delete cascade on update cascade,
  foreign key(class_id) references class_info(class_id) on delete cascade on update cascade
);

create table homework_info(
	homework_id varchar(15),
	class_id varchar(15),
	stu_id varchar(15),
	pcourse_id varchar(15),
	done int,
	comment text,
	store_url char(255),
	primary key(homework_id),
	foreign key(class_id) references class_info(class_id) on delete cascade on update cascade,
	foreign key(stu_id) references student_info(stu_id) on delete cascade on update cascade,
	foreign key(pcourse_id) references percourse_info(pcourse_id) on delete cascade on update cascade
);
