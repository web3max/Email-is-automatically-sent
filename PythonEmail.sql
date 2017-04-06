/*
Navicat MySQL Data Transfer

Source Server         : 腾讯云
Source Server Version : 50536
Source Host           : 119.29.175.124:3306
Source Database       : pythonemail

Target Server Type    : MYSQL
Target Server Version : 50536
File Encoding         : 65001

Date: 2017-04-06 22:17:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for hlh_giftcard
-- ----------------------------
DROP TABLE IF EXISTS `hlh_giftcard`;
CREATE TABLE `hlh_giftcard` (
  `ID` int(10) NOT NULL AUTO_INCREMENT COMMENT '实体卡id',
  `CardName` varchar(20) DEFAULT NULL COMMENT '卡名称',
  `SchemaID` int(10) DEFAULT NULL COMMENT '方案ID',
  `CardNO` varchar(10) NOT NULL COMMENT '卡号',
  `ExchgCode` varchar(10) DEFAULT NULL COMMENT '兑换码',
  `ExchgDate` datetime DEFAULT NULL COMMENT '兑换时间',
  `SalePrice` decimal(8,2) DEFAULT NULL COMMENT 'V卡销售价格',
  `NeedExchgCde` varchar(2) DEFAULT 'Y' COMMENT '是否需要兑换码Y需要N不需要',
  `DispatchID` int(10) DEFAULT NULL COMMENT '工单id',
  `IsActive` varchar(2) NOT NULL DEFAULT 'N' COMMENT '激活状态 N未激活 Y已激活',
  `IsExchg` varchar(2) NOT NULL DEFAULT 'N' COMMENT '兑换状态 N未兑换 Y已兑换',
  `IsShipping` varchar(2) NOT NULL DEFAULT 'N' COMMENT '发货状态 N 未发货  Y 已发货',
  `ActiveBy` varchar(10) DEFAULT NULL COMMENT '激活人',
  `ActiveDate` datetime DEFAULT NULL COMMENT '激活时间',
  `CreateBy` varchar(10) DEFAULT NULL COMMENT '创建人',
  `CreateDate` datetime DEFAULT NULL COMMENT '创建时间',
  `LastUpdBy` varchar(10) DEFAULT NULL COMMENT '最后更新人',
  `LastUpdDt` datetime DEFAULT NULL COMMENT '最后更新时间',
  `CustomerName` varchar(20) DEFAULT NULL COMMENT '客户名称',
  `cust_id` int(10) DEFAULT NULL COMMENT '客户id',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Idx_HLH_GiftCard_cardno` (`CardNO`),
  UNIQUE KEY `idx_HLH_GiftCard_ExchgCode` (`ExchgCode`),
  KEY `Idx_HLH_GiftCard_IsActive` (`IsActive`),
  KEY `Idx_HLH_GiftCard_IsExchg` (`IsExchg`),
  KEY `Idx_HLH_GiftCard_IsShipping` (`IsShipping`),
  KEY `Idx_HLH_GiftCard_cust_id` (`cust_id`),
  KEY `Idx_HLH_GiftCard_CustomerName` (`CustomerName`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='实体卡表';

-- ----------------------------
-- Records of hlh_giftcard
-- ----------------------------
INSERT INTO `hlh_giftcard` VALUES ('114', '知味', '9', '0000000042', 'NZ86WQ94', '2017-02-24 10:46:13', '125.00', 'Y', null, 'Y', 'Y', 'Y', 'admin', '2017-02-23 18:24:37', 'admin', '2017-02-23 18:09:05', 'admin', '2017-03-31 21:07:05', '龙辉', '10');

-- ----------------------------
-- Table structure for hlh_giftcardexchg
-- ----------------------------
DROP TABLE IF EXISTS `hlh_giftcardexchg`;
CREATE TABLE `hlh_giftcardexchg` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `GiftCardID` int(10) DEFAULT NULL COMMENT '品牌实体卡id',
  `ShippingBy` varchar(10) DEFAULT NULL COMMENT '收货人',
  `MobileNO` varchar(20) DEFAULT NULL COMMENT '手机号码',
  `ShippingAdress` varchar(500) DEFAULT NULL COMMENT '收货地址',
  `ShipOrderNo` varchar(50) DEFAULT NULL COMMENT '发货单号',
  `ExpressCompanyName` varchar(200) DEFAULT NULL COMMENT '发货公司名称',
  `ProductName` varchar(50) DEFAULT NULL COMMENT '产品名称',
  `ShippingDate` datetime DEFAULT NULL COMMENT '发货时间',
  `CreateBy` varchar(10) DEFAULT NULL COMMENT '创建人',
  `CreateDate` datetime DEFAULT NULL COMMENT '创建时间',
  `LastUpdBy` varchar(10) DEFAULT NULL COMMENT '最后更新人',
  `LastUpdDt` datetime DEFAULT NULL COMMENT '最后更新时间',
  `ShippingTo` varchar(10) DEFAULT NULL COMMENT '发货人',
  `ProductImage` char(120) DEFAULT NULL COMMENT '产品图片暂时使用传数据用，后期可删除',
  `Province` varchar(20) DEFAULT NULL COMMENT '省份',
  `City` varchar(20) DEFAULT NULL COMMENT '城市',
  `Area` varchar(20) DEFAULT NULL COMMENT '地区',
  `ExchgDate` datetime DEFAULT NULL COMMENT '兑换日期临时使用的，后期可删除',
  `ShippingRemark` varchar(200) DEFAULT NULL COMMENT '收礼人发货备注',
  PRIMARY KEY (`ID`),
  KEY `idx_HLH_GiftCardExchg_GiftCardID` (`GiftCardID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='礼品卡兑换信息表';

-- ----------------------------
-- Records of hlh_giftcardexchg
-- ----------------------------
INSERT INTO `hlh_giftcardexchg` VALUES ('27', '114', 'admin', '15918560619', 'Test', '4124315', '456', '天然绿檀雕花木梳', '2017-02-24 10:46:13', 'admin', '2017-02-24 10:46:13', 'admin', '2017-03-31 21:47:46', 'Max', 'http://www.runoob.com/wp-content/themes/runoob/assets/img/runoob-logo.png', '内蒙古自治区', '呼和浩特市', '土默特左旗', '2017-03-23 21:46:10', '');

-- ----------------------------
-- Table structure for hlh_mnssetting
-- ----------------------------
DROP TABLE IF EXISTS `hlh_mnssetting`;
CREATE TABLE `hlh_mnssetting` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `MNSCode` varchar(20) DEFAULT NULL COMMENT '消息编号',
  `MNSName` varchar(50) DEFAULT NULL COMMENT '消息名称',
  `SITCode` varchar(50) DEFAULT NULL COMMENT 'SIT环境编号',
  `UATCode` varchar(50) DEFAULT NULL COMMENT 'UAT环境编号',
  `PRODCode` varchar(50) DEFAULT NULL COMMENT '正式环境编号',
  `TriggerConditon` varchar(200) DEFAULT NULL COMMENT '触发条件',
  `FormatType` varchar(50) DEFAULT NULL COMMENT '格式类型',
  `MNSContent` varchar(50) DEFAULT NULL COMMENT '内容',
  `CreateBy` varchar(10) DEFAULT NULL COMMENT '创建人',
  `CreateDate` datetime DEFAULT NULL COMMENT '创建时间',
  `LastUpdBy` varchar(10) DEFAULT NULL COMMENT '最后更新人',
  `LastUpdDt` datetime DEFAULT NULL COMMENT '最后更新时间',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `IDX_HLH_MNSSetting_MNSCode` (`MNSCode`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of hlh_mnssetting
-- ----------------------------
INSERT INTO `hlh_mnssetting` VALUES ('4', '0001', '激活', 'SIT-TOPIC-VKActive', 'UAT-TOPIC-VKActive', 'PROD-TOPIC-VKActive', '激活成功', 'json', 'HLH_GiftCard记录', 'system', '2017-03-08 15:08:14', 'system', '2017-03-31 21:56:10');
INSERT INTO `hlh_mnssetting` VALUES ('5', '0002', '兑换', 'SIT-TOPIC-VKExchange', 'UAT-TOPIC-VKExchange', 'PROD-TOPIC-VKExchange', '兑换成功', 'json', 'HLH_GiftCard记录', 'system', '2017-03-08 15:08:14', 'system', '2017-03-31 21:56:13');
INSERT INTO `hlh_mnssetting` VALUES ('6', '0003', '发货', 'SIT-TOPIC-VKShipped', 'UAT-TOPIC-VKShipped', 'PROD-TOPIC-VKShipped', '点击发货', 'json', 'HLH_GiftCard记录', 'system', '2017-03-08 15:08:14', 'system', '2017-03-31 21:56:19');

-- ----------------------------
-- Table structure for hlh_mnssublog
-- ----------------------------
DROP TABLE IF EXISTS `hlh_mnssublog`;
CREATE TABLE `hlh_mnssublog` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `MNSPubID` int(10) DEFAULT NULL COMMENT '发送ID',
  `MNSSubID` int(10) DEFAULT NULL COMMENT '接收编号',
  `SubDate` datetime DEFAULT NULL COMMENT '接收日期',
  `SubContent` varchar(2000) DEFAULT NULL COMMENT '接收内容Json',
  `SubStatus` varchar(2) DEFAULT NULL COMMENT '成功Y失败N',
  `ErrContent` varchar(500) DEFAULT NULL COMMENT '错误信息',
  PRIMARY KEY (`ID`),
  KEY `idx_HLH_MNSSubLog_MNSSubID` (`MNSSubID`),
  KEY `idx_HLH_MNSSubLog_MNSPubID` (`MNSPubID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='订阅日志者日志';

-- ----------------------------
-- Records of hlh_mnssublog
-- ----------------------------
INSERT INTO `hlh_mnssublog` VALUES ('97', '283', '3', '2017-04-06 21:09:13', '{\"status\":\"Y\",content:\"邮件发送成功\"}', 'Y', '');

-- ----------------------------
-- Table structure for hlh_schema
-- ----------------------------
DROP TABLE IF EXISTS `hlh_schema`;
CREATE TABLE `hlh_schema` (
  `ID` int(10) NOT NULL AUTO_INCREMENT COMMENT '套餐方案',
  `SchmNo` varchar(10) DEFAULT NULL COMMENT '方案编号',
  `SchemaType` varchar(20) DEFAULT NULL COMMENT '方案类型(字典表002)',
  `SchmName` varchar(10) NOT NULL COMMENT '套餐名称',
  `SchemaStatus` varchar(20) DEFAULT 'ONL' COMMENT '方案状态（字典表003）',
  `CustomerName` varchar(20) DEFAULT NULL COMMENT '客户名称',
  `H5Link` varchar(200) DEFAULT NULL COMMENT 'H5贺卡链接',
  `ProdListLink` varchar(255) DEFAULT NULL COMMENT '产品列表链接',
  `Price` decimal(8,2) DEFAULT NULL COMMENT '套餐价格',
  `From_Name` varchar(50) DEFAULT NULL COMMENT '送礼人',
  `Blessing` varchar(400) DEFAULT NULL COMMENT '祝福语',
  `To_Name` varchar(50) DEFAULT NULL COMMENT '收礼人',
  `CreateBy` varchar(10) DEFAULT NULL COMMENT '创建人',
  `CreateDate` datetime DEFAULT NULL COMMENT '创建时间',
  `LastUpdBy` varchar(10) DEFAULT NULL COMMENT '最后更新人',
  `LastUpdDt` datetime DEFAULT NULL COMMENT '最后更新时间',
  `Customer_id` int(10) DEFAULT NULL COMMENT '客户id',
  `MareketPrice` decimal(8,2) DEFAULT NULL COMMENT '市场价格',
  `StckOnHand` int(10) DEFAULT '0' COMMENT '方案库存',
  `SalesSum` int(10) DEFAULT NULL COMMENT '累计销售数量',
  `SchemaMusicId` int(10) DEFAULT NULL COMMENT '选择音乐ID',
  `wxShareTitle` varchar(50) DEFAULT NULL COMMENT '微信分享标题',
  `wxShareDesc` varchar(200) DEFAULT NULL COMMENT '微信分享简介',
  `H5CardID` int(10) DEFAULT NULL COMMENT '选择的H5贺卡类别',
  `Incolorcode` varchar(10) DEFAULT NULL COMMENT '内部颜色代码',
  `outcolorcode` varchar(10) DEFAULT NULL COMMENT '外部颜色代码',
  `VcardTxt` varchar(400) DEFAULT NULL COMMENT 'V卡文本',
  `cust_id` int(10) DEFAULT NULL COMMENT '客户ID',
  PRIMARY KEY (`ID`),
  KEY `idx_HLH_Schema_cust_id` (`cust_id`),
  KEY `idx_HLH_Schema_CustomerName` (`CustomerName`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='好礼汇V卡方案';

-- ----------------------------
-- Records of hlh_schema
-- ----------------------------
INSERT INTO `hlh_schema` VALUES ('9', 'G000005', 'GEN', '指纹', 'ONL', 'Max', 'Heka:170322_shine', 'Plan:birth108', '100.00', '你好', '七情不昧四重恩，八筏常归十界魂。负业诸尘贤劫渡，无边水月大千存。', '你好', 'admin', '2017-03-06 17:50:47', '', '2017-03-31 21:51:45', null, null, '0', null, null, null, null, null, null, null, null, '14');
SET FOREIGN_KEY_CHECKS=1;