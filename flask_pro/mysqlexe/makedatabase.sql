create database childreading;
use childreading;

DROP TABLE IF EXISTS student_info;

create table student_info(
	stu_id varchar(15) COMMENT '微信的openid',
	credit int COMMENT '学生获得的积分',
	qresult varchar(50) COMMENT '问卷调查的结果',
	rec_result varchar(25) COMMENT '推荐结果',
	primary key(stu_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学生信息表';

DROP TABLE IF EXISTS teacher_info;

create table teacher_info(
	tea_id varchar(15) COMMENT '教师的id',
	tea_email varchar(50) COMMENT '教师的email',
	tea_name varchar(25) COMMENT '教师的姓名',
	password varchar(25) COMMENT '教师端的登陆密码',
	teacher_intro varchar(255) COMMENT '教师的简介',
	primary key(tea_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='教师信息表';

DROP TABLE IF EXISTS setcourse_info;

create table setcourse_info(
	scourse_id varchar(15) COMMENT '套课的id',
	scourse_title varchar(60) COMMENT '套课的标题',
	scourse_theme varchar(50) COMMENT '套课所属的主题',
	scourse_stage varchar(50) COMMENT '套课适合的年龄阶段',
	pageimg_urls varchar(255) COMMENT '套课封面图片的url地址',
	scourse_intro varchar(255) COMMENT '套课的介绍',
	buylink varchar(255) COMMENT '套课相关书籍的购买链接',
	scourse_credit int COMMENT '套课的积分',
	scourse_price decimal (10,2) COMMENT '套课的价格',
	primary key(scourse_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='套课信息表';

DROP TABLE IF EXISTS percourse_info;

create table percourse_info(
	pcourse_id varchar(15) COMMENT '单课的id',
	pcourse_name varchar(50) COMMENT '单课的名称',
	vedio_url varchar(255)COMMENT '单课相关视频的url地址',
	pcourse_intro text COMMENT '单课的简介',
	pcourse_pageimgurl varchar(255) COMMENT '单课封面的地址',
	type varchar(20) COMMENT '课程的类型 图画书还是文字书',
	year varchar(4) COMMENT '课程适合的年级',
	theme varchar(30)COMMENT '课程的主题',
	price decimal(6,2) COMMENT '单课的价格',
	primary key(pcourse_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='单课信息表';

DROP TABLE IF EXISTS s_p_class_info;

create table s_p_class_info(
	id int COMMENT '自增主键' AUTO_INCREMENT,
	scourse_id varchar(15) COMMENT '套课id',
	pcourse_id varchar(15) COMMENT '单课id',
	thenumber int(2) COMMENT '单课在该套课中的节次',
	primary key(id),
	foreign key(scourse_id) references setcourse_info(scourse_id) on delete cascade on update cascade,
	foreign key(pcourse_id) references percourse_info(pcourse_id) on delete cascade on update cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='套课组成信息表';

DROP TABLE IF EXISTS problems;

create table problems(
	pro_id int COMMENT '自增主键 题号' AUTO_INCREMENT,
	pro_stem text COMMENT '题干',
	choice text COMMENT '选项内容',
	answer char(1) COMMENT '答案 A,B,C,D',
	flag int COMMENT '标记是否是主观题  主观题（1）  客观题（0）',
	scourse_id varchar(15) COMMENT '哪个套课包含了这道题',
	pcourse_id varchar(15) COMMENT '哪节单课包含了这道题',
	pro_num varchar(15) COMMENT '在单课的一套习题中，该题的题号',
	primary key(pro_id) COMMENT '',
	foreign key(scourse_id) references setcourse_info(scourse_id) on delete cascade on update cascade,
	foreign key(pcourse_id) references percourse_info(pcourse_id) on delete cascade on update cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='题库表';

DROP TABLE IF EXISTS class_info;

create table class_info(
	class_id varchar(15) COMMENT '班级号',
	tea_id varchar(15) COMMENT '任课教师',
	scourse_id varchar(15) COMMENT '该班级的配套课程',
	start_time date COMMENT '开始时间',
	end_time date COMMENT '结束时间',
	primary key(class_id),
	foreign key(tea_id) references teacher_info(tea_id) on delete cascade on update cascade,
	foreign key(scourse_id) references setcourse_info(scourse_id) on delete cascade on update cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='班级信息表';

DROP TABLE IF EXISTS takes_table;

create table takes_table(
	stu_id varchar(15) COMMENT '学生id',
	scourse_id varchar(15) COMMENT '套课id',
	stage int COMMENT '学生当前在该课程的哪个阶段，上到第几节课',
	foreign key(scourse_id) references setcourse_info(scourse_id) on delete cascade on update cascade,
	foreign key(stu_id) references student_info(stu_id) on delete cascade on update cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学生的选课情况表';

DROP TABLE IF EXISTS inclass;

create table inclass(
  stu_id varchar (15) COMMENT '学生id',
  class_id varchar (15) COMMENT '班级id',
  foreign key(stu_id) references student_info(stu_id) on delete cascade on update cascade,
  foreign key(class_id) references class_info(class_id) on delete cascade on update cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学生所在班级的信息表';

DROP TABLE IF EXISTS homework_info;

create table homework_info(
	homework_id varchar(15) COMMENT '条目的id',
	class_id varchar(15) COMMENT '班级id',
	stu_id varchar(15) COMMENT '学生id',
	pcourse_id varchar(15) COMMENT '单课id',
	done int COMMENT '标记位  已提交,已批改（3） 已提交，未批改（2） 未提交，未批改（1）',
	comment text COMMENT '老师的批改结果',
	store_url char(255) COMMENT '学生上传的url地址',
	primary key(homework_id) COMMENT '',
	foreign key(class_id) references class_info(class_id) on delete cascade on update cascade,
	foreign key(stu_id) references student_info(stu_id) on delete cascade on update cascade,
	foreign key(pcourse_id) references percourse_info(pcourse_id) on delete cascade on update cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='作业信息表';
