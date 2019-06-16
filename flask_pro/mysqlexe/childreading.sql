/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : childreading

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2019-06-16 02:11:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for class_info
-- ----------------------------
DROP TABLE IF EXISTS `class_info`;
CREATE TABLE `class_info` (
  `class_id` varchar(15) NOT NULL COMMENT '班级号',
  `tea_id` varchar(15) DEFAULT NULL COMMENT '任课教师',
  `scourse_id` varchar(15) DEFAULT NULL COMMENT '该班级的配套课程',
  `start_time` date DEFAULT NULL COMMENT '开始时间',
  `end_time` date DEFAULT NULL COMMENT '结束时间',
  `stage` int(11) DEFAULT '1' COMMENT '当前课程进行到的阶段',
  `class_name` varchar(255) DEFAULT NULL COMMENT '班级的名字',
  PRIMARY KEY (`class_id`),
  KEY `tea_id` (`tea_id`),
  KEY `scourse_id` (`scourse_id`),
  CONSTRAINT `class_info_ibfk_1` FOREIGN KEY (`tea_id`) REFERENCES `teacher_info` (`tea_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `class_info_ibfk_2` FOREIGN KEY (`scourse_id`) REFERENCES `setcourse_info` (`scourse_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='班级信息表';

-- ----------------------------
-- Table structure for homework_info
-- ----------------------------
DROP TABLE IF EXISTS `homework_info`;
CREATE TABLE `homework_info` (
  `homework_id` varchar(15) NOT NULL COMMENT '条目的id',
  `class_id` varchar(15) DEFAULT NULL COMMENT '班级id',
  `stu_id` varchar(30) DEFAULT NULL COMMENT '学生id',
  `pcourse_id` varchar(15) DEFAULT NULL COMMENT '单课id',
  `done` int(11) DEFAULT NULL COMMENT '标记位  已提交,已批改（3） 已提交，未批改（2） 未提交，未批改（1）',
  `comment` text COMMENT '老师的批改结果',
  `store_url` char(255) DEFAULT NULL COMMENT '学生上传的url地址',
  PRIMARY KEY (`homework_id`),
  KEY `class_id` (`class_id`),
  KEY `stu_id` (`stu_id`),
  KEY `pcourse_id` (`pcourse_id`),
  CONSTRAINT `homework_info_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class_info` (`class_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `homework_info_ibfk_2` FOREIGN KEY (`stu_id`) REFERENCES `student_info` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `homework_info_ibfk_3` FOREIGN KEY (`pcourse_id`) REFERENCES `percourse_info` (`pcourse_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='作业信息表';

-- ----------------------------
-- Table structure for inclass
-- ----------------------------
DROP TABLE IF EXISTS `inclass`;
CREATE TABLE `inclass` (
  `stu_id` varchar(30) DEFAULT NULL COMMENT '学生id',
  `class_id` varchar(15) DEFAULT NULL COMMENT '班级id',
  KEY `stu_id` (`stu_id`),
  KEY `class_id` (`class_id`),
  CONSTRAINT `inclass_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `student_info` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `inclass_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `class_info` (`class_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学生所在班级的信息表';

-- ----------------------------
-- Table structure for percourse_info
-- ----------------------------
DROP TABLE IF EXISTS `percourse_info`;
CREATE TABLE `percourse_info` (
  `pcourse_id` varchar(15) NOT NULL COMMENT '单课的id',
  `pcourse_name` varchar(50) DEFAULT NULL COMMENT '单课的名称',
  `vedio_url` varchar(255) DEFAULT NULL COMMENT '单课相关视频的url地址',
  `pcourse_intro` text COMMENT '单课的简介',
  `pcourse_pageimgurl` varchar(255) DEFAULT NULL COMMENT '单课封面的地址',
  `type` varchar(20) DEFAULT NULL COMMENT '课程的类型 图画书还是文字书',
  `year` varchar(4) DEFAULT NULL COMMENT '课程适合的年级',
  `theme` varchar(30) DEFAULT NULL COMMENT '课程的主题',
  `price` decimal(6,2) DEFAULT '100.00' COMMENT '单课的价格',
  PRIMARY KEY (`pcourse_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='单课信息表';

-- ----------------------------
-- Table structure for problems
-- ----------------------------
DROP TABLE IF EXISTS `problems`;
CREATE TABLE `problems` (
  `pro_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增主键 题号',
  `pro_stem` text COMMENT '题干',
  `choice` text COMMENT '选项内容',
  `answer` char(1) DEFAULT NULL COMMENT '答案 A,B,C,D',
  `flag` int(11) DEFAULT NULL COMMENT '标记是否是主观题  主观题（1）  客观题（0）',
  `scourse_id` varchar(15) DEFAULT NULL COMMENT '哪个套课包含了这道题',
  `pcourse_id` varchar(15) DEFAULT NULL COMMENT '哪节单课包含了这道题',
  `pro_num` varchar(15) DEFAULT NULL COMMENT '在单课的一套习题中，该题的题号',
  PRIMARY KEY (`pro_id`),
  KEY `scourse_id` (`scourse_id`),
  KEY `pcourse_id` (`pcourse_id`),
  CONSTRAINT `problems_ibfk_1` FOREIGN KEY (`scourse_id`) REFERENCES `setcourse_info` (`scourse_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `problems_ibfk_2` FOREIGN KEY (`pcourse_id`) REFERENCES `percourse_info` (`pcourse_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='题库表';

-- ----------------------------
-- Table structure for setcourse_info
-- ----------------------------
DROP TABLE IF EXISTS `setcourse_info`;
CREATE TABLE `setcourse_info` (
  `scourse_id` varchar(15) NOT NULL COMMENT '套课的id',
  `scourse_title` varchar(60) DEFAULT NULL COMMENT '套课的标题',
  `scourse_theme` varchar(50) DEFAULT NULL COMMENT '套课所属的主题',
  `scourse_stage` varchar(50) DEFAULT NULL COMMENT '套课适合的年龄阶段，最小的适合年龄',
  `pageimg_urls` varchar(255) DEFAULT NULL COMMENT '套课封面图片的url地址',
  `scourse_intro` varchar(255) DEFAULT NULL COMMENT '套课的介绍',
  `buylink` varchar(255) DEFAULT NULL COMMENT '套课相关书籍的购买链接',
  `scourse_credit` int(11) DEFAULT '0' COMMENT '套课的积分',
  `scourse_price` decimal(10,2) DEFAULT '100.00' COMMENT '套课的价格',
  PRIMARY KEY (`scourse_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='套课信息表';

-- ----------------------------
-- Table structure for student_info
-- ----------------------------
DROP TABLE IF EXISTS `student_info`;
CREATE TABLE `student_info` (
  `stu_id` varchar(30) NOT NULL COMMENT '微信的openid',
  `credit` int(11) DEFAULT '0' COMMENT '学生获得的积分',
  `qresult` varchar(50) DEFAULT NULL COMMENT '问卷调查的结果',
  `rec_result` varchar(25) DEFAULT NULL COMMENT '推荐结果',
  PRIMARY KEY (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学生信息表';

-- ----------------------------
-- Table structure for s_p_class_info
-- ----------------------------
DROP TABLE IF EXISTS `s_p_class_info`;
CREATE TABLE `s_p_class_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `scourse_id` varchar(15) DEFAULT NULL COMMENT '套课id',
  `pcourse_id` varchar(15) DEFAULT NULL COMMENT '单课id',
  `thenumber` int(2) DEFAULT NULL COMMENT '单课在该套课中的节次',
  PRIMARY KEY (`id`),
  KEY `scourse_id` (`scourse_id`),
  KEY `pcourse_id` (`pcourse_id`),
  CONSTRAINT `s_p_class_info_ibfk_1` FOREIGN KEY (`scourse_id`) REFERENCES `setcourse_info` (`scourse_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `s_p_class_info_ibfk_2` FOREIGN KEY (`pcourse_id`) REFERENCES `percourse_info` (`pcourse_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COMMENT='套课组成信息表';

-- ----------------------------
-- Table structure for takes_pcourse
-- ----------------------------
DROP TABLE IF EXISTS `takes_pcourse`;
CREATE TABLE `takes_pcourse` (
  `stu_id` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `pcourse_id` varchar(15) CHARACTER SET utf8mb4 NOT NULL COMMENT '学生选择的单课的情况',
  KEY `qweqwevew` (`stu_id`),
  KEY `wqeqwe` (`pcourse_id`),
  CONSTRAINT `qweqwevew` FOREIGN KEY (`stu_id`) REFERENCES `student_info` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `wqeqwe` FOREIGN KEY (`pcourse_id`) REFERENCES `percourse_info` (`pcourse_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for teacher_info
-- ----------------------------
DROP TABLE IF EXISTS `teacher_info`;
CREATE TABLE `teacher_info` (
  `tea_id` varchar(15) NOT NULL COMMENT '教师的id',
  `tea_email` varchar(50) DEFAULT NULL COMMENT '教师的email',
  `tea_name` varchar(25) DEFAULT NULL COMMENT '教师的姓名',
  `password` varchar(25) DEFAULT NULL COMMENT '教师端的登陆密码',
  `teacher_intro` varchar(255) DEFAULT NULL COMMENT '教师的简介',
  PRIMARY KEY (`tea_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='教师信息表';

-- ----------------------------
-- View structure for stu_class
-- ----------------------------
DROP VIEW IF EXISTS `stu_class`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `stu_class` AS select `a`.`stu_id` AS `stu_id`,`a`.`class_id` AS `class_id`,`b`.`class_name` AS `class_name`,`b`.`stage` AS `stage` from (`inclass` `a` join `class_info` `b` on((`a`.`class_id` = `b`.`class_id`))) ;

-- ----------------------------
-- View structure for tea_class
-- ----------------------------
DROP VIEW IF EXISTS `tea_class`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `tea_class` AS select `a`.`class_id` AS `class_id`,`a`.`scourse_id` AS `scourse_id`,`c`.`scourse_title` AS `scourse_title`,`b`.`tea_name` AS `tea_name`,`b`.`teacher_intro` AS `teacher_intro`,`a`.`start_time` AS `start_time`,`a`.`end_time` AS `end_time` from ((`class_info` `a` join `teacher_info` `b` on((`a`.`tea_id` = `b`.`tea_id`))) join `setcourse_info` `c` on((`c`.`scourse_id` = `a`.`scourse_id`))) ;
DROP TRIGGER IF EXISTS `class_take_insert_before_trigger`;
DELIMITER ;;
CREATE TRIGGER `class_take_insert_before_trigger` BEFORE INSERT ON `inclass` FOR EACH ROW begin
	if(new.stu_id not in (select stu_id from student_info)) then
	insert student_info(stu_id) values(new.stu_id);
	end if;


end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `pcourse_take_insert_before_trigger`;
DELIMITER ;;
CREATE TRIGGER `pcourse_take_insert_before_trigger` BEFORE INSERT ON `takes_pcourse` FOR EACH ROW begin
	if(new.stu_id not in (select stu_id from student_info)) then
	insert student_info(stu_id) values(new.stu_id);
	end if;


end
;;
DELIMITER ;
