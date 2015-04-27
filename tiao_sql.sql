PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2015-04-17 17:39:37.614831');
INSERT INTO "django_migrations" VALUES(2,'auth','0001_initial','2015-04-17 17:39:37.708667');
INSERT INTO "django_migrations" VALUES(3,'ssl_users','0001_initial','2015-04-17 17:39:37.805091');
INSERT INTO "django_migrations" VALUES(4,'admin','0001_initial','2015-04-17 17:39:37.906846');
INSERT INTO "django_migrations" VALUES(5,'sessions','0001_initial','2015-04-17 17:39:37.935448');
INSERT INTO "django_migrations" VALUES(6,'ssl_users','0002_auto_20150417_1803','2015-04-17 18:03:26.483227');
INSERT INTO "django_migrations" VALUES(7,'ssl_users','0003_auto_20150419_1524','2015-04-19 15:24:28.325056');
INSERT INTO "django_migrations" VALUES(8,'ssl_users','0004_user_items_table_itemdescription','2015-04-20 02:41:12.223221');
INSERT INTO "django_migrations" VALUES(9,'ssl_users','0005_auto_20150420_0248','2015-04-20 02:48:22.584691');
INSERT INTO "django_migrations" VALUES(10,'ssl_users','0006_auto_20150420_0410','2015-04-20 04:10:28.395732');
INSERT INTO "django_migrations" VALUES(11,'display_items','0001_initial','2015-04-20 04:27:09.147556');
INSERT INTO "django_migrations" VALUES(12,'display_items','0002_auto_20150420_0428','2015-04-20 04:28:29.173436');
INSERT INTO "django_migrations" VALUES(13,'display_items','0003_auto_20150421_0700','2015-04-21 07:00:17.657047');
INSERT INTO "django_migrations" VALUES(14,'ssl_users','0007_user_items_table_istradesuccess','2015-04-22 03:05:03.796066');
INSERT INTO "django_migrations" VALUES(15,'display_items','0004_item_messages_table','2015-04-22 03:26:26.008910');
INSERT INTO "django_migrations" VALUES(16,'display_items','0005_comments_table','2015-04-22 04:09:28.772345');
INSERT INTO "django_migrations" VALUES(17,'display_items','0006_comments_table_itempostusername','2015-04-22 06:27:07.377148');
INSERT INTO "django_migrations" VALUES(18,'ssl_users','0008_tzy_users_realname','2015-04-23 20:31:08.538630');
INSERT INTO "django_migrations" VALUES(19,'ssl_users','0009_tzy_users_avatarurl','2015-04-23 20:42:09.498340');
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL, UNIQUE ("app_label", "model"));
INSERT INTO "django_content_type" VALUES(1,'log entry','admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'permission','auth','permission');
INSERT INTO "django_content_type" VALUES(3,'group','auth','group');
INSERT INTO "django_content_type" VALUES(4,'content type','contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(5,'session','sessions','session');
INSERT INTO "django_content_type" VALUES(6,'user','ssl_users','tzy_users');
INSERT INTO "django_content_type" VALUES(7,'user_items_table','ssl_users','user_items_table');
INSERT INTO "django_content_type" VALUES(8,'ask_info_table','display_items','ask_info_table');
INSERT INTO "django_content_type" VALUES(9,'item_messages_table','display_items','item_messages_table');
INSERT INTO "django_content_type" VALUES(10,'comments_table','display_items','comments_table');
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, UNIQUE ("content_type_id", "codename"));
INSERT INTO "auth_permission" VALUES(1,'Can add log entry',1,'add_logentry');
INSERT INTO "auth_permission" VALUES(2,'Can change log entry',1,'change_logentry');
INSERT INTO "auth_permission" VALUES(3,'Can delete log entry',1,'delete_logentry');
INSERT INTO "auth_permission" VALUES(4,'Can add permission',2,'add_permission');
INSERT INTO "auth_permission" VALUES(5,'Can change permission',2,'change_permission');
INSERT INTO "auth_permission" VALUES(6,'Can delete permission',2,'delete_permission');
INSERT INTO "auth_permission" VALUES(7,'Can add group',3,'add_group');
INSERT INTO "auth_permission" VALUES(8,'Can change group',3,'change_group');
INSERT INTO "auth_permission" VALUES(9,'Can delete group',3,'delete_group');
INSERT INTO "auth_permission" VALUES(10,'Can add content type',4,'add_contenttype');
INSERT INTO "auth_permission" VALUES(11,'Can change content type',4,'change_contenttype');
INSERT INTO "auth_permission" VALUES(12,'Can delete content type',4,'delete_contenttype');
INSERT INTO "auth_permission" VALUES(13,'Can add session',5,'add_session');
INSERT INTO "auth_permission" VALUES(14,'Can change session',5,'change_session');
INSERT INTO "auth_permission" VALUES(15,'Can delete session',5,'delete_session');
INSERT INTO "auth_permission" VALUES(16,'Can add user',6,'add_tzy_users');
INSERT INTO "auth_permission" VALUES(17,'Can change user',6,'change_tzy_users');
INSERT INTO "auth_permission" VALUES(18,'Can delete user',6,'delete_tzy_users');
INSERT INTO "auth_permission" VALUES(19,'Can add user_items_table',7,'add_user_items_table');
INSERT INTO "auth_permission" VALUES(20,'Can change user_items_table',7,'change_user_items_table');
INSERT INTO "auth_permission" VALUES(21,'Can delete user_items_table',7,'delete_user_items_table');
INSERT INTO "auth_permission" VALUES(22,'Can add ask_info_table',8,'add_ask_info_table');
INSERT INTO "auth_permission" VALUES(23,'Can change ask_info_table',8,'change_ask_info_table');
INSERT INTO "auth_permission" VALUES(24,'Can delete ask_info_table',8,'delete_ask_info_table');
INSERT INTO "auth_permission" VALUES(25,'Can add item_messages_table',9,'add_item_messages_table');
INSERT INTO "auth_permission" VALUES(26,'Can change item_messages_table',9,'change_item_messages_table');
INSERT INTO "auth_permission" VALUES(27,'Can delete item_messages_table',9,'delete_item_messages_table');
INSERT INTO "auth_permission" VALUES(28,'Can add comments_table',10,'add_comments_table');
INSERT INTO "auth_permission" VALUES(29,'Can change comments_table',10,'change_comments_table');
INSERT INTO "auth_permission" VALUES(30,'Can delete comments_table',10,'delete_comments_table');
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("group_id", "permission_id"));
CREATE TABLE "ssl_users_tzy_users_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tzy_users_id" integer NOT NULL REFERENCES "ssl_users_tzy_users" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), UNIQUE ("tzy_users_id", "group_id"));
CREATE TABLE "ssl_users_tzy_users_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tzy_users_id" integer NOT NULL REFERENCES "ssl_users_tzy_users" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("tzy_users_id", "permission_id"));
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "ssl_users_tzy_users" ("id"));
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO "django_session" VALUES('essi2xb5ntz257au846jt5zote2yd02h','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-01 18:17:18.589761');
INSERT INTO "django_session" VALUES('q74w5qneqe7plopo82gxe97ymihzk8ky','YWM3ZGM2MTZlNzEzOTUwY2VjMDhlNTAzYzBkYjJmODA0ZDFmOTI5ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFjODViNDY1OTE2YjU5YzU4YzRmMzAxMjQ5MWUwMWNlOWU4Mjc5ZmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-05-02 01:27:04.322929');
INSERT INTO "django_session" VALUES('flxcl71d2l5kqbskdlngp7jgimg3324b','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:37.036675');
INSERT INTO "django_session" VALUES('tfdc0x4t9sky0sfg69umv94664ikp0xs','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:37.354780');
INSERT INTO "django_session" VALUES('bjialzn80h4jx8p802lp5hc6w2cr5hln','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:37.715680');
INSERT INTO "django_session" VALUES('by6tg2qj1hssslhkotfum20qqv9ppx7b','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:38.140480');
INSERT INTO "django_session" VALUES('kd91etxgnln7l8hdgcnmaja41eazd49n','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:38.497953');
INSERT INTO "django_session" VALUES('wwursa9yseftudldt8wv08dymuefaigz','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:39.361797');
INSERT INTO "django_session" VALUES('qrttotsaadzd2votloqjk7nsj1j2x3kb','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:40.191341');
INSERT INTO "django_session" VALUES('1mpy2ue35s4d7i22c6cvw485rmeoouy1','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:41.508879');
INSERT INTO "django_session" VALUES('loza8rx59ym1wlx3t143s1xqqqwrai0w','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:43.091316');
INSERT INTO "django_session" VALUES('hed2fdtz85yfqzddxtqk938stwyo3j0b','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:45.283417');
INSERT INTO "django_session" VALUES('gpwynyskatsujfcfd8el7d9ngzhx0rji','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:47.426467');
INSERT INTO "django_session" VALUES('ekviqtzf5vdvdbid97m83bkk4y4ek54p','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:50.545973');
INSERT INTO "django_session" VALUES('nr50ncrn1n0iaf8iiuse7d5ghy1njlan','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-03 15:59:54.448041');
INSERT INTO "django_session" VALUES('0y9w480euubbhzxic7ol3vkc1nbrewgf','YWM3ZGM2MTZlNzEzOTUwY2VjMDhlNTAzYzBkYjJmODA0ZDFmOTI5ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFjODViNDY1OTE2YjU5YzU4YzRmMzAxMjQ5MWUwMWNlOWU4Mjc5ZmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-05-04 19:16:07.412935');
INSERT INTO "django_session" VALUES('rnxa8lc0vg0cubuyiguj5jcvu8dqdfrz','YWM3ZGM2MTZlNzEzOTUwY2VjMDhlNTAzYzBkYjJmODA0ZDFmOTI5ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFjODViNDY1OTE2YjU5YzU4YzRmMzAxMjQ5MWUwMWNlOWU4Mjc5ZmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-05-07 04:09:56.701259');
INSERT INTO "django_session" VALUES('0ax25eiw1dhgcxb7f7g2sgerpvl02eg2','NjBhYTc0Y2I0ZmE3Y2E2OWMzMWQwN2FhNzM3OGRhMzVhZjllMmU4ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjcyNTYwMDNhNWUxZmEzNDVmZDZlMWVlMWM1ZGY4ODczOWU1MmVmYTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjZ9','2015-05-09 01:42:35.382512');
INSERT INTO "django_session" VALUES('ubukqch6ti4b9vtw4g429ihu264pho3u','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-09 16:28:19.768109');
INSERT INTO "django_session" VALUES('2ptq3df3w65z006s7ay9c4lhxnoh23mf','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-09 17:00:37.906516');
INSERT INTO "django_session" VALUES('r601869b202lvjrkztt9cuj9fex4tybx','YmE4MjdlYTRmOTczNDg2N2I2YjVmMDJkOTE5NDRjMjYyNGVhM2Q5ODp7fQ==','2015-05-09 17:00:41.180463');
INSERT INTO "django_session" VALUES('9hej4pbuw5aj9bcw7iwxuey0lyiwwvnh','YWM3ZGM2MTZlNzEzOTUwY2VjMDhlNTAzYzBkYjJmODA0ZDFmOTI5ZTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFjODViNDY1OTE2YjU5YzU4YzRmMzAxMjQ5MWUwMWNlOWU4Mjc5ZmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-05-10 08:20:59.449522');
CREATE TABLE "display_items_ask_info_table" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "TzyUser_id" integer NULL REFERENCES "ssl_users_tzy_users" ("id"), "ItemId" varchar(100) NOT NULL UNIQUE, "ItemTitle" text NOT NULL, "ClickCount" integer NOT NULL, "PostTime" integer NOT NULL, "IsBlock" bool NOT NULL, "ContactUserName" varchar(100) NOT NULL, "ContactUserPhone" varchar(20) NOT NULL, "ItemType" varchar(20) NOT NULL, "LikeList" text NOT NULL, "LikeCount" integer NOT NULL, "ReportList" text NOT NULL, "ReportReason" text NOT NULL, "ItemDescription" text NOT NULL);
INSERT INTO "display_items_ask_info_table" VALUES(7,NULL,'69fb7f18d887cc27212b41161fc4ece2','需要一台电子琴',0,1429600739,0,'','15201519357','','[]',0,'[]','','');
INSERT INTO "display_items_ask_info_table" VALUES(8,NULL,'14c6dff4583fbf4ec90f4ff9544489ab','求购一辆二手山地车',0,1429600794,0,'','15201519357','','[]',0,'[]','','女式的最好,男士的也没问题');
INSERT INTO "display_items_ask_info_table" VALUES(9,6,'dbd91f9ca89128d7700b25fa51719f93','求购网球拍',0,1429600818,0,'','18101360342','','[]',0,'[]','','');
INSERT INTO "display_items_ask_info_table" VALUES(10,1,'1d98dcf25e430902dd8070e5e800fce1','dada',0,1429674751,0,'','15201519357','','[]',0,'[]','','');
INSERT INTO "display_items_ask_info_table" VALUES(11,6,'486cd9bd695be083d61720aeb0db97f0','dada',0,1429979329,0,'','18101360342','','[]',0,'[]','','');
CREATE TABLE "ssl_users_user_items_table" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "IsTradeSuccess" bool NOT NULL, "ItemId" varchar(100) NOT NULL UNIQUE, "ItemName" varchar(100) NOT NULL, "ItemOldPrice" integer NOT NULL, "ItemPrice" integer NOT NULL, "ItemsNum" integer NOT NULL, "ItemImageUrls" text NOT NULL, "ClickCount" integer NOT NULL, "PostTime" integer NOT NULL, "LastEditTime" integer NOT NULL, "IsBlock" bool NOT NULL, "Feature" varchar(100) NOT NULL, "ItemType" varchar(20) NOT NULL, "LikeList" text NOT NULL, "LikeCount" integer NOT NULL, "ReportList" text NOT NULL, "ReportReason" text NOT NULL, "TzyUser_id" integer NOT NULL REFERENCES "ssl_users_tzy_users" ("id"), "ItemDescription" text NOT NULL, "ContactUserName" varchar(100) NOT NULL, "ContactUserPhone" varchar(20) NOT NULL);
INSERT INTO "ssl_users_user_items_table" VALUES(15,0,'256b201aee57082bc89c0fe62889927b','GRE词汇精选',39,10,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/ubHHRnMPe-tkqysxNDI5NTc5MTU4"]',22,1429579158,1429579158,0,'全新','100','[]',0,'[]','',6,'GRE词汇经典红宝书','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(16,0,'c770964c429bc49fa75ab90eecc55cea','英语报刊选读教程',30,10,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/X94BROFrWObrPCsxNDI5NTc5Njc1"]',0,1429579675,1429579675,0,'全新','100','[]',0,'[]','',6,'英语课外书','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(17,0,'31f9f6a666e02829ad8c1dd05b3c3c87','英语演讲艺术',20,5,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/9EdtYg2hLP90WCsxNDI5NTg0ODkw"]',0,1429584890,1429584890,0,'全新','100','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(18,0,'b670817ed50a0c90c04a6109a4577073','微积分学习指导---典型例题精解',30,10,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/_6PulpMnhlfBXisxNDI5NTg1MDk2"]',0,1429585096,1429585096,0,'全新','101','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(19,0,'5be86a787792957b1d2832842dac0122','线性代数与空间几何学习精讲',40,15,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/R0t10CAagiL-NCsxNDI5NTg1MTM4"]',0,1429585138,1429585138,0,'全新','101','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(20,0,'332d905e5bbc8c6aaf148f1315897729','力学(物理类)',35,10,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/hPW6kx8_RLvYHisxNDI5NTg1MTY5"]',0,1429585169,1429585169,0,'全新','101','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(21,0,'e8a1c2b1a8b70ebe460b087112a19663','大学数学第二版随机数学',20,8,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/QqyLChnDN5MNAisxNDI5NTg1NjM1"]',0,1429585635,1429585635,0,'全新','101','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(22,0,'141c5358c71bdb5cc0b745d954ba95f7','信号与系统上册',40,15,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/VSxKHeL3n5ka_isxNDI5NTg2MTEz"]',0,1429586113,1429586113,0,'全新','102','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(23,0,'8066a9044417ba31559bd1b879a9a3a3','信号与系统下册',40,15,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/MH1l_lZQuja_LysxNDI5NTg2MTI3"]',0,1429586127,1429586127,0,'全新','102','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(24,0,'2a350ca35b3e400c502c278c7253adfc','信号与系统习题解答',35,12,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/qvNrQw0Yz4CCISsxNDI5NTg2MTYy"]',0,1429586162,1429586162,0,'全新','102','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(25,0,'d2d55632300980c69c48abdb6ce61b42','毛泽东思想和中国特色社会主义理论体系概论',25,8,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/AnvhWeRMDdXfsisxNDI5NTg2MjUw"]',0,1429586250,1429586250,0,'全新','103','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(26,0,'b7b169f69d67cf67a865282f5a07aa2f','中国近现代史纲要',20,5,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/M3FKjymJFA8X0CsxNDI5NTg2Mjgx"]',0,1429586281,1429586281,0,'全新','103','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(27,0,'39c2f482dcaa269d3a581f38ee7e08b2','马克思主义基本原理概论',20,5,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/OxDJXfxBDGa8rSsxNDI5NTg2MzE2"]',0,1429586316,1429586316,0,'全新','103','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(28,0,'cb7164ca33d4031f673273a68f5b176a','思想道德修养与法律基础',20,5,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/_DxTSJj_vObkzSsxNDI5NTg2Mzgy"]',2,1429586382,1429586382,0,'全新','103','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(29,0,'2ef6e77ed29995afbc9316d0d72689ce','经济学原理第5版(上)',38,25,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/TuJn8HPbBu3KnSsxNDI5NTg2NDc0"]',0,1429586474,1429586474,0,'全新','104','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(30,0,'b5250168671de39a9f3fb594b790ce68','经济学原理第5版(下)',35,25,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/3H2yvYta0QTZhSsxNDI5NTg2NTIw"]',539,1429586520,1429586520,0,'全新','104','[]',0,'[]','',6,'','尚书林','18101360342');
INSERT INTO "ssl_users_user_items_table" VALUES(31,0,'93ae9d410294a062010a247fea41a4a3','宏观经济学:现代观点',40,20,1,'["http://upload-items.oss-cn-beijing.aliyuncs.com/C-6lmP1p_wkRwisxNDI5NTg2NTU0"]',67,1429586554,1429586554,0,'全新','104','[]',0,'[]','',6,'','尚书林','18101360342');
CREATE TABLE "display_items_item_messages_table" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "MessageId" varchar(100) NOT NULL UNIQUE, "Message" text NOT NULL, "PostTime" integer NOT NULL, "IsBlock" bool NOT NULL, "LikeList" text NOT NULL, "LikeCount" integer NOT NULL, "ReportList" text NOT NULL, "ReportReason" text NOT NULL, "Item_id" integer NOT NULL REFERENCES "ssl_users_user_items_table" ("id"), "TzyUser_id" integer NULL REFERENCES "ssl_users_tzy_users" ("id"));
INSERT INTO "display_items_item_messages_table" VALUES(5,'fc1ff04bbf8d82590d29c36806c18090','哈哈',1429718630,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(6,'99aa10323557dc3df27c1b1d91c704ce','哈哈',1429718670,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(7,'7a932cdd476c91cf848fb7507e02ee28','喜欢这本书,浅显易懂',1429755771,0,'[]',0,'[]','',30,6);
INSERT INTO "display_items_item_messages_table" VALUES(8,'53d9bff2d01f1a7fc6cd5d83b6c83194','尝试一下',1429758939,0,'[]',0,'[]','',30,6);
INSERT INTO "display_items_item_messages_table" VALUES(9,'977e69588a4668da1e96b5e9a1f7fdb1','试试看',1429758970,0,'[]',0,'[]','',30,NULL);
INSERT INTO "display_items_item_messages_table" VALUES(10,'6a2d8e7ae8b3144b350600f8676a3be5','我就是过客',1429758979,0,'[]',0,'[]','',30,NULL);
INSERT INTO "display_items_item_messages_table" VALUES(11,'34e913f8f24e0b5abaf769aeacfd35a9','试一试',1429759258,0,'[]',0,'[]','',30,NULL);
INSERT INTO "display_items_item_messages_table" VALUES(12,'a88b853d407d3ffa729cc0df81ebf4fd','哈哈',1429759264,0,'[]',0,'[]','',30,NULL);
INSERT INTO "display_items_item_messages_table" VALUES(13,'3435da63dd4f55c87c92b2cac853484a','大山',1429759268,0,'[]',0,'[]','',30,NULL);
INSERT INTO "display_items_item_messages_table" VALUES(14,'6cc3765ce57b44aeb33b463b937d9caf','大山',1429759271,0,'[]',0,'[]','',30,NULL);
INSERT INTO "display_items_item_messages_table" VALUES(15,'b62ce51fbcb2c9664fdde3a12549c07d','再来一条',1429759282,0,'[]',0,'[]','',30,NULL);
INSERT INTO "display_items_item_messages_table" VALUES(16,'17394989b8f783914597a2011156af57','我也来试试',1429806165,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(17,'6fd3f1fb048cb5dc00cbc308ee11d298','哈哈',1429806174,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(18,'2aaf2f2989a0ebc31a48964915fc6ef0','测试1',1429806231,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(19,'000440e90cf0a429a225609dfc6e74dd','测试2',1429806322,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(20,'5f015ccf2ed57499ee32b073cd2d6d79','测试3',1429806367,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(21,'acd01a5344bb6b29497fa96b73d8d207','测试4',1429806399,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(22,'9082e14956d38a4705ce4f752047b371','测试5',1429806422,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(23,'9980bcdd3ed4c8ee7c9eb7b82a12644a','测试6',1429806441,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(24,'d0f5e9ee800c4f6853d67142358fa672','测试7',1429806449,0,'[]',0,'[]','',30,1);
INSERT INTO "display_items_item_messages_table" VALUES(25,'605b583e390181fb0fa038c52d6edd2d','dada',1429816661,0,'[]',0,'[]','',30,7);
INSERT INTO "display_items_item_messages_table" VALUES(26,'90515b4fc736a2c13241722d485dfaf3','dada',1429979366,0,'[]',0,'[]','',30,6);
INSERT INTO "display_items_item_messages_table" VALUES(27,'2b92a959491db20235c2ebdb47cfdb08','dada',1429979371,0,'[]',0,'[]','',30,6);
INSERT INTO "display_items_item_messages_table" VALUES(28,'d2b6c66ce968baf08582ecd95314ce26','aa',1429979375,0,'[]',0,'[]','',30,6);
CREATE TABLE "display_items_comments_table" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "ItemPostUsername" varchar(100) NOT NULL, "CommentId" varchar(100) NOT NULL UNIQUE, "Message" text NOT NULL, "PostTime" integer NOT NULL, "Grade" real NOT NULL, "IsDelete" bool NOT NULL, "CommentUser_id" integer NOT NULL REFERENCES "ssl_users_tzy_users" ("id"), "Item_id" integer NOT NULL REFERENCES "ssl_users_user_items_table" ("id"));
CREATE TABLE "ssl_users_tzy_users" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "AvatarUrl" varchar(100) NOT NULL, "password" varchar(128) NOT NULL, "last_login" datetime NOT NULL, "is_superuser" bool NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "Mobilephone" varchar(20) NOT NULL, "QQ" integer NOT NULL, "Nickname" varchar(20) NOT NULL, "IsStudent" bool NOT NULL, "RealName" varchar(50) NOT NULL);
INSERT INTO "ssl_users_tzy_users" VALUES(1,'','pbkdf2_sha256$15000$khNe0wcYW7ua$mZpY55+eCOiWiVdf9SxMBgaa2kc2eC1oXufTvX2DfQM=','2015-04-26 08:20:59.434532',1,'jing','','','1544299536@qq.com',1,1,'2015-04-17 17:40:00.444858','',0,'',1,'');
INSERT INTO "ssl_users_tzy_users" VALUES(6,'http://upload-items.oss-cn-beijing.aliyuncs.com/K29cNPWAz79DOisxNDI5OTM5NzYy','pbkdf2_sha256$15000$7cYCQNAr8gur$s7eqfR2w/q0O9XS5Sg3Xhp/yF213ToTTfsA5NQoZ/XM=','2015-04-25 17:00:47.525149',0,'尚书林','','','',0,1,'2015-04-17 19:11:10.791721','18101360342',1544299536,'尚书林',1,'尚书');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('django_content_type',10);
INSERT INTO "sqlite_sequence" VALUES('django_migrations',19);
INSERT INTO "sqlite_sequence" VALUES('auth_permission',30);
INSERT INTO "sqlite_sequence" VALUES('display_items_ask_info_table',11);
INSERT INTO "sqlite_sequence" VALUES('ssl_users_user_items_table',33);
INSERT INTO "sqlite_sequence" VALUES('display_items_comments_table',0);
INSERT INTO "sqlite_sequence" VALUES('display_items_item_messages_table',28);
INSERT INTO "sqlite_sequence" VALUES('ssl_users_tzy_users',11);
CREATE INDEX "auth_permission_417f1b1c" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_0e939a4f" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_8373b171" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "ssl_users_tzy_users_groups_1367ea9f" ON "ssl_users_tzy_users_groups" ("tzy_users_id");
CREATE INDEX "ssl_users_tzy_users_groups_0e939a4f" ON "ssl_users_tzy_users_groups" ("group_id");
CREATE INDEX "ssl_users_tzy_users_user_permissions_1367ea9f" ON "ssl_users_tzy_users_user_permissions" ("tzy_users_id");
CREATE INDEX "ssl_users_tzy_users_user_permissions_8373b171" ON "ssl_users_tzy_users_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_417f1b1c" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_e8701ad4" ON "django_admin_log" ("user_id");
CREATE INDEX "django_session_de54fa62" ON "django_session" ("expire_date");
CREATE INDEX "display_items_ask_info_table_e32da77b" ON "display_items_ask_info_table" ("TzyUser_id");
CREATE INDEX "ssl_users_user_items_table_e32da77b" ON "ssl_users_user_items_table" ("TzyUser_id");
CREATE INDEX "display_items_item_messages_table_1e1f102a" ON "display_items_item_messages_table" ("Item_id");
CREATE INDEX "display_items_item_messages_table_e32da77b" ON "display_items_item_messages_table" ("TzyUser_id");
CREATE INDEX "display_items_comments_table_4f353f1b" ON "display_items_comments_table" ("CommentUser_id");
CREATE INDEX "display_items_comments_table_1e1f102a" ON "display_items_comments_table" ("Item_id");
COMMIT;