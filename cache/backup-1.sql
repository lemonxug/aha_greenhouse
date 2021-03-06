PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "monitor_devicecategory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "index" integer NOT NULL);
INSERT INTO monitor_devicecategory VALUES(1,'传感器',0);
INSERT INTO monitor_devicecategory VALUES(2,'温室遮光',0);
INSERT INTO monitor_devicecategory VALUES(3,'卷帘机',0);
INSERT INTO monitor_devicecategory VALUES(4,'风机',0);
INSERT INTO monitor_devicecategory VALUES(5,'喷淋灌溉',0);
INSERT INTO monitor_devicecategory VALUES(6,'加温',0);
INSERT INTO monitor_devicecategory VALUES(7,'补光',0);
INSERT INTO monitor_devicecategory VALUES(8,'补充CO2',0);
INSERT INTO monitor_devicecategory VALUES(9,'杀虫灯',0);
CREATE TABLE IF NOT EXISTS "monitor_environmentindicator" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
INSERT INTO monitor_environmentindicator VALUES(1,'温度');
INSERT INTO monitor_environmentindicator VALUES(2,'湿度');
INSERT INTO monitor_environmentindicator VALUES(3,'CO2浓度');
INSERT INTO monitor_environmentindicator VALUES(4,'光照强度');
INSERT INTO monitor_environmentindicator VALUES(5,'土壤水分');
INSERT INTO monitor_environmentindicator VALUES(6,'PH值');
CREATE TABLE IF NOT EXISTS "monitor_greenhouse" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL);
INSERT INTO monitor_greenhouse VALUES(1,'1号大棚');
INSERT INTO monitor_greenhouse VALUES(2,'2号大棚');
INSERT INTO monitor_greenhouse VALUES(3,'3号大棚');
INSERT INTO monitor_greenhouse VALUES(4,'4号大棚');
INSERT INTO monitor_greenhouse VALUES(5,'5号大棚');
INSERT INTO monitor_greenhouse VALUES(6,'6号大棚');
INSERT INTO monitor_greenhouse VALUES(7,'7号大棚');
INSERT INTO monitor_greenhouse VALUES(8,'8号大棚');
INSERT INTO monitor_greenhouse VALUES(9,'9号大棚');
CREATE TABLE IF NOT EXISTS "monitor_environmentdata" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "value" decimal NOT NULL, "create_time" datetime NOT NULL, "device_id" bigint NULL REFERENCES "monitor_device" ("id") DEFERRABLE INITIALLY DEFERRED, "indicator_id" bigint NULL REFERENCES "monitor_environmentindicator" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO monitor_environmentdata VALUES(1,'27.7693778627711',datetime('2021-05-07  12:14:48'),3,1);
INSERT INTO monitor_environmentdata VALUES(2,'20.58311841482',datetime('2021-05-07  12:14:48'),4,1);
INSERT INTO monitor_environmentdata VALUES(3,'29.2856358746237',datetime('2021-05-07  12:14:48'),13,1);
INSERT INTO monitor_environmentdata VALUES(4,'28.1514512128449',datetime('2021-05-07  12:14:48'),14,1);
INSERT INTO monitor_environmentdata VALUES(5,'28.9747635944769',datetime('2021-05-07  12:14:48'),23,1);
INSERT INTO monitor_environmentdata VALUES(6,'33.1670095877947',datetime('2021-05-07  12:14:48'),24,1);
INSERT INTO monitor_environmentdata VALUES(7,'32.333735043106',datetime('2021-05-07  12:19:48'),3,1);
INSERT INTO monitor_environmentdata VALUES(8,'26.6198558112134',datetime('2021-05-07  12:19:48'),4,1);
INSERT INTO monitor_environmentdata VALUES(9,'29.977223721546',datetime('2021-05-07  12:19:48'),13,1);
INSERT INTO monitor_environmentdata VALUES(10,'29.7763699928975',datetime('2021-05-07  12:19:48'),14,1);
INSERT INTO monitor_environmentdata VALUES(11,'33.5099147242113',datetime('2021-05-07  12:19:48'),23,1);
INSERT INTO monitor_environmentdata VALUES(12,'34.1604270939717',datetime('2021-05-07  12:19:48'),24,1);
INSERT INTO monitor_environmentdata VALUES(13,'29.6694734181646',datetime('2021-05-07  12:24:48'),3,1);
INSERT INTO monitor_environmentdata VALUES(14,'25.0493067860021',datetime('2021-05-07  12:24:48'),4,1);
INSERT INTO monitor_environmentdata VALUES(15,'23.821822033999',datetime('2021-05-07  12:24:48'),13,1);
INSERT INTO monitor_environmentdata VALUES(16,'26.3832760552995',datetime('2021-05-07  12:24:48'),14,1);
INSERT INTO monitor_environmentdata VALUES(17,'34.6768315734939',datetime('2021-05-07  12:24:48'),23,1);
INSERT INTO monitor_environmentdata VALUES(18,'32.4827018134938',datetime('2021-05-07  12:24:48'),24,1);
INSERT INTO monitor_environmentdata VALUES(19,'31.6377766755998',datetime('2021-05-07  12:29:48'),3,1);
INSERT INTO monitor_environmentdata VALUES(20,'33.4209793191011',datetime('2021-05-07  12:29:48'),4,1);
INSERT INTO monitor_environmentdata VALUES(21,'25.2427247561912',datetime('2021-05-07  12:29:48'),13,1);
INSERT INTO monitor_environmentdata VALUES(22,'32.9976276203576',datetime('2021-05-07  12:29:48'),14,1);
INSERT INTO monitor_environmentdata VALUES(23,'27.4784064243736',datetime('2021-05-07  12:29:48'),23,1);
INSERT INTO monitor_environmentdata VALUES(24,'28.7340537696721',datetime('2021-05-07  12:29:48'),24,1);
INSERT INTO monitor_environmentdata VALUES(25,'26.4816571653106',datetime('2021-05-07  12:34:48'),3,1);
INSERT INTO monitor_environmentdata VALUES(26,'34.6354709440993',datetime('2021-05-07  12:34:48'),4,1);
INSERT INTO monitor_environmentdata VALUES(27,'26.076853316607',datetime('2021-05-07  12:34:48'),13,1);
INSERT INTO monitor_environmentdata VALUES(28,'27.9573076213261',datetime('2021-05-07  12:34:48'),14,1);
INSERT INTO monitor_environmentdata VALUES(29,'29.8895004482356',datetime('2021-05-07  12:34:48'),23,1);
INSERT INTO monitor_environmentdata VALUES(30,'34.9348350684016',datetime('2021-05-07  12:34:48'),24,1);
INSERT INTO monitor_environmentdata VALUES(31,'19.5882223669308',datetime('2021-05-07  12:14:48'),1,2);
INSERT INTO monitor_environmentdata VALUES(32,'12.4925140196886',datetime('2021-05-07  12:14:48'),2,2);
INSERT INTO monitor_environmentdata VALUES(33,'17.0482303691351',datetime('2021-05-07  12:14:48'),11,2);
INSERT INTO monitor_environmentdata VALUES(34,'10.2433231407998',datetime('2021-05-07  12:14:48'),12,2);
INSERT INTO monitor_environmentdata VALUES(35,'11.0007567441669',datetime('2021-05-07  12:14:48'),21,2);
INSERT INTO monitor_environmentdata VALUES(36,'12.3074139353584',datetime('2021-05-07  12:14:48'),22,2);
INSERT INTO monitor_environmentdata VALUES(37,'18.3758880577623',datetime('2021-05-07  12:19:48'),1,2);
INSERT INTO monitor_environmentdata VALUES(38,'20.0211941036616',datetime('2021-05-07  12:19:48'),2,2);
INSERT INTO monitor_environmentdata VALUES(39,'15.8668766440971',datetime('2021-05-07  12:19:48'),11,2);
INSERT INTO monitor_environmentdata VALUES(40,'12.4239230053893',datetime('2021-05-07  12:19:48'),12,2);
INSERT INTO monitor_environmentdata VALUES(41,'19.6419366992044',datetime('2021-05-07  12:19:48'),21,2);
INSERT INTO monitor_environmentdata VALUES(42,'15.2231827714993',datetime('2021-05-07  12:19:48'),22,2);
INSERT INTO monitor_environmentdata VALUES(43,'12.9022261702216',datetime('2021-05-07  12:24:48'),1,2);
INSERT INTO monitor_environmentdata VALUES(44,'20.7688495400614',datetime('2021-05-07  12:24:48'),2,2);
INSERT INTO monitor_environmentdata VALUES(45,'11.7158962660065',datetime('2021-05-07  12:24:48'),11,2);
INSERT INTO monitor_environmentdata VALUES(46,'12.0935119933412',datetime('2021-05-07  12:24:48'),12,2);
INSERT INTO monitor_environmentdata VALUES(47,'18.4831787756461',datetime('2021-05-07  12:24:48'),21,2);
INSERT INTO monitor_environmentdata VALUES(48,'12.521051743985',datetime('2021-05-07  12:24:48'),22,2);
INSERT INTO monitor_environmentdata VALUES(49,'15.7216775317714',datetime('2021-05-07  12:29:48'),1,2);
INSERT INTO monitor_environmentdata VALUES(50,'15.8524745963226',datetime('2021-05-07  12:29:48'),2,2);
INSERT INTO monitor_environmentdata VALUES(51,'20.6000766082028',datetime('2021-05-07  12:29:48'),11,2);
INSERT INTO monitor_environmentdata VALUES(52,'12.193223496653',datetime('2021-05-07  12:29:48'),12,2);
INSERT INTO monitor_environmentdata VALUES(53,'19.9666403105206',datetime('2021-05-07  12:29:48'),21,2);
INSERT INTO monitor_environmentdata VALUES(54,'16.0673957191939',datetime('2021-05-07  12:29:48'),22,2);
INSERT INTO monitor_environmentdata VALUES(55,'15.3008079346323',datetime('2021-05-07  12:34:48'),1,2);
INSERT INTO monitor_environmentdata VALUES(56,'14.7362661455581',datetime('2021-05-07  12:34:48'),2,2);
INSERT INTO monitor_environmentdata VALUES(57,'11.8982531825098',datetime('2021-05-07  12:34:48'),11,2);
INSERT INTO monitor_environmentdata VALUES(58,'14.3258969012508',datetime('2021-05-07  12:34:48'),12,2);
INSERT INTO monitor_environmentdata VALUES(59,'14.5980215328031',datetime('2021-05-07  12:34:48'),21,2);
INSERT INTO monitor_environmentdata VALUES(60,'19.164880077161',datetime('2021-05-07  12:34:48'),22,2);
INSERT INTO monitor_environmentdata VALUES(61,'539',datetime('2021-05-07  12:14:48'),5,3);
INSERT INTO monitor_environmentdata VALUES(62,'542',datetime('2021-05-07  12:14:48'),15,3);
INSERT INTO monitor_environmentdata VALUES(63,'640',datetime('2021-05-07  12:14:48'),25,3);
INSERT INTO monitor_environmentdata VALUES(64,'659',datetime('2021-05-07  12:24:48'),5,3);
INSERT INTO monitor_environmentdata VALUES(65,'591',datetime('2021-05-07  12:24:48'),15,3);
INSERT INTO monitor_environmentdata VALUES(66,'537',datetime('2021-05-07  12:24:48'),25,3);
INSERT INTO monitor_environmentdata VALUES(67,'686',datetime('2021-05-07  12:34:48'),5,3);
INSERT INTO monitor_environmentdata VALUES(68,'515',datetime('2021-05-07  12:34:48'),15,3);
INSERT INTO monitor_environmentdata VALUES(69,'644',datetime('2021-05-07  12:34:48'),25,3);
INSERT INTO monitor_environmentdata VALUES(70,'48.7785416298113',datetime('2021-05-07  12:14:48'),6,4);
INSERT INTO monitor_environmentdata VALUES(71,'49.7147838677812',datetime('2021-05-07  12:14:48'),16,4);
INSERT INTO monitor_environmentdata VALUES(72,'40.0909397615809',datetime('2021-05-07  12:14:48'),26,4);
INSERT INTO monitor_environmentdata VALUES(73,'48.7127524956813',datetime('2021-05-07  12:24:48'),6,4);
INSERT INTO monitor_environmentdata VALUES(74,'49.5675341235904',datetime('2021-05-07  12:24:48'),16,4);
INSERT INTO monitor_environmentdata VALUES(75,'44.368821376688',datetime('2021-05-07  12:24:48'),26,4);
INSERT INTO monitor_environmentdata VALUES(76,'48.953013401539',datetime('2021-05-07  12:34:48'),6,4);
INSERT INTO monitor_environmentdata VALUES(77,'47.8950068385343',datetime('2021-05-07  12:34:48'),16,4);
INSERT INTO monitor_environmentdata VALUES(78,'46.2271415014878',datetime('2021-05-07  12:34:48'),26,4);
INSERT INTO monitor_environmentdata VALUES(79,'5.69617587671883',datetime('2021-05-07  12:14:48'),7,5);
INSERT INTO monitor_environmentdata VALUES(80,'7.81640341804954',datetime('2021-05-07  12:14:48'),8,5);
INSERT INTO monitor_environmentdata VALUES(81,'8.73307111942159',datetime('2021-05-07  12:14:48'),17,5);
INSERT INTO monitor_environmentdata VALUES(82,'7.64096506315506',datetime('2021-05-07  12:14:48'),18,5);
INSERT INTO monitor_environmentdata VALUES(83,'7.04019834653796',datetime('2021-05-07  12:14:48'),27,5);
INSERT INTO monitor_environmentdata VALUES(84,'10.8348133159513',datetime('2021-05-07  12:14:48'),28,5);
INSERT INTO monitor_environmentdata VALUES(85,'8.87266571206345',datetime('2021-05-07  12:24:48'),7,5);
INSERT INTO monitor_environmentdata VALUES(86,'6.67089100270277',datetime('2021-05-07  12:24:48'),8,5);
INSERT INTO monitor_environmentdata VALUES(87,'8.24351209586059',datetime('2021-05-07  12:24:48'),17,5);
INSERT INTO monitor_environmentdata VALUES(88,'5.01133749613272',datetime('2021-05-07  12:24:48'),18,5);
INSERT INTO monitor_environmentdata VALUES(89,'10.4056232321589',datetime('2021-05-07  12:24:48'),27,5);
INSERT INTO monitor_environmentdata VALUES(90,'9.8501405248202',datetime('2021-05-07  12:24:48'),28,5);
INSERT INTO monitor_environmentdata VALUES(91,'10.2290532723289',datetime('2021-05-07  12:34:48'),7,5);
INSERT INTO monitor_environmentdata VALUES(92,'8.34159200436372',datetime('2021-05-07  12:34:48'),8,5);
INSERT INTO monitor_environmentdata VALUES(93,'6.34375471557272',datetime('2021-05-07  12:34:48'),17,5);
INSERT INTO monitor_environmentdata VALUES(94,'7.32095762128049',datetime('2021-05-07  12:34:48'),18,5);
INSERT INTO monitor_environmentdata VALUES(95,'8.56433983486539',datetime('2021-05-07  12:34:48'),27,5);
INSERT INTO monitor_environmentdata VALUES(96,'7.61092343496332',datetime('2021-05-07  12:34:48'),28,5);
INSERT INTO monitor_environmentdata VALUES(97,'10.4171628324565',datetime('2021-05-07  12:14:48'),9,6);
INSERT INTO monitor_environmentdata VALUES(98,'8.927046655443',datetime('2021-05-07  12:14:48'),10,6);
INSERT INTO monitor_environmentdata VALUES(99,'8.79161989507641',datetime('2021-05-07  12:14:48'),19,6);
INSERT INTO monitor_environmentdata VALUES(100,'6.97114946122911',datetime('2021-05-07  12:14:48'),20,6);
INSERT INTO monitor_environmentdata VALUES(101,'9.7792253813961',datetime('2021-05-07  12:14:48'),29,6);
INSERT INTO monitor_environmentdata VALUES(102,'8.03898505804925',datetime('2021-05-07  12:14:48'),30,6);
INSERT INTO monitor_environmentdata VALUES(103,'7.54248341616953',datetime('2021-05-07  12:24:48'),9,6);
INSERT INTO monitor_environmentdata VALUES(104,'10.2157762069947',datetime('2021-05-07  12:24:48'),10,6);
INSERT INTO monitor_environmentdata VALUES(105,'5.13535008089743',datetime('2021-05-07  12:24:48'),19,6);
INSERT INTO monitor_environmentdata VALUES(106,'5.65674112919643',datetime('2021-05-07  12:24:48'),20,6);
INSERT INTO monitor_environmentdata VALUES(107,'10.4242223985301',datetime('2021-05-07  12:24:48'),29,6);
INSERT INTO monitor_environmentdata VALUES(108,'5.18570005012363',datetime('2021-05-07  12:24:48'),30,6);
INSERT INTO monitor_environmentdata VALUES(109,'10.3626331569233',datetime('2021-05-07  12:34:48'),9,6);
INSERT INTO monitor_environmentdata VALUES(110,'5.10049961766468',datetime('2021-05-07  12:34:48'),10,6);
INSERT INTO monitor_environmentdata VALUES(111,'9.79052248023853',datetime('2021-05-07  12:34:48'),19,6);
INSERT INTO monitor_environmentdata VALUES(112,'8.25195627663954',datetime('2021-05-07  12:34:48'),20,6);
INSERT INTO monitor_environmentdata VALUES(113,'10.6114043232028',datetime('2021-05-07  12:34:48'),29,6);
INSERT INTO monitor_environmentdata VALUES(114,'8.42656395540891',datetime('2021-05-07  12:34:48'),30,6);
CREATE TABLE IF NOT EXISTS "monitor_device" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "location" varchar(100) NOT NULL, "status" varchar(100) NOT NULL, "is_active" bool NOT NULL, "category_id" bigint NULL REFERENCES "monitor_devicecategory" ("id") DEFERRABLE INITIALLY DEFERRED, "greenhouse_id" bigint NULL REFERENCES "monitor_greenhouse" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO monitor_device VALUES(1,'大棚1-湿度1','1号大棚南','正常',1,1,1);
INSERT INTO monitor_device VALUES(2,'大棚1-湿度2','1号大棚北','正常',1,1,1);
INSERT INTO monitor_device VALUES(3,'大棚1-温度1','1号大棚南','正常',1,1,1);
INSERT INTO monitor_device VALUES(4,'大棚1-温度2','1号大棚北','正常',1,1,1);
INSERT INTO monitor_device VALUES(5,'大棚1-CO2','1号大棚中','正常',1,1,1);
INSERT INTO monitor_device VALUES(6,'大棚1-光照','1号大棚中','正常',1,1,1);
INSERT INTO monitor_device VALUES(7,'大棚1-土壤水分1','1号大棚南','正常',1,1,1);
INSERT INTO monitor_device VALUES(8,'大棚1-土壤水分2','1号大棚北','正常',1,1,1);
INSERT INTO monitor_device VALUES(9,'大棚1-PH1','1号大棚南','正常',1,1,1);
INSERT INTO monitor_device VALUES(10,'大棚1-PH2','1号大棚北','正常',1,1,1);
INSERT INTO monitor_device VALUES(11,'大棚2-湿度1','2号大棚南','正常',1,1,2);
INSERT INTO monitor_device VALUES(12,'大棚2-湿度2','2号大棚北','正常',1,1,2);
INSERT INTO monitor_device VALUES(13,'大棚2-温度1','2号大棚南','正常',1,1,2);
INSERT INTO monitor_device VALUES(14,'大棚2-温度2','2号大棚北','正常',1,1,2);
INSERT INTO monitor_device VALUES(15,'大棚2-CO2','2号大棚中','正常',1,1,2);
INSERT INTO monitor_device VALUES(16,'大棚2-光照','2号大棚中','正常',1,1,2);
INSERT INTO monitor_device VALUES(17,'大棚2-土壤水分1','2号大棚南','正常',1,1,2);
INSERT INTO monitor_device VALUES(18,'大棚2-土壤水分2','2号大棚北','正常',1,1,2);
INSERT INTO monitor_device VALUES(19,'大棚2-PH1','2号大棚南','正常',1,1,2);
INSERT INTO monitor_device VALUES(20,'大棚2-PH2','2号大棚北','正常',1,1,2);
INSERT INTO monitor_device VALUES(21,'大棚3-湿度1','3号大棚南','正常',1,1,3);
INSERT INTO monitor_device VALUES(22,'大棚3-湿度2','3号大棚北','正常',1,1,3);
INSERT INTO monitor_device VALUES(23,'大棚3-温度1','3号大棚南','正常',1,1,3);
INSERT INTO monitor_device VALUES(24,'大棚3-温度2','3号大棚北','正常',1,1,3);
INSERT INTO monitor_device VALUES(25,'大棚3-CO2','3号大棚中','正常',1,1,3);
INSERT INTO monitor_device VALUES(26,'大棚3-光照','3号大棚中','正常',1,1,3);
INSERT INTO monitor_device VALUES(27,'大棚3-土壤水分1','3号大棚南','正常',1,1,3);
INSERT INTO monitor_device VALUES(28,'大棚3-土壤水分2','3号大棚北','正常',1,1,3);
INSERT INTO monitor_device VALUES(29,'大棚3-PH1','3号大棚南','正常',1,1,3);
INSERT INTO monitor_device VALUES(30,'大棚3-PH2','3号大棚北','正常',1,1,3);
CREATE INDEX "monitor_environmentdata_device_id_d922c2a5" ON "monitor_environmentdata" ("device_id");
CREATE INDEX "monitor_environmentdata_indicator_id_a2dd58fd" ON "monitor_environmentdata" ("indicator_id");
CREATE INDEX "monitor_device_category_id_49234b48" ON "monitor_device" ("category_id");
CREATE INDEX "monitor_device_greenhouse_id_21e85bf1" ON "monitor_device" ("greenhouse_id");
COMMIT;
