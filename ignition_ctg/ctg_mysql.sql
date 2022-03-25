DROP TABLE IF EXISTS `ctg_active_client`;
CREATE TABLE  `ctg_active_client` (
  `Client_ID` varchar(45) NOT NULL default '',
  `PointID` varchar(255) NOT NULL default '',
  PRIMARY KEY  (`PointID`,`Client_ID`)
);

DROP TABLE IF EXISTS `ctg_axes`;
CREATE TABLE  `ctg_axes` (
  `ndx` int(11) NOT NULL auto_increment,
  `NAME` varchar(45) NOT NULL,
  `LABEL` varchar(45) NOT NULL,
  `TYPE` varchar(45) NOT NULL,
  `LABEL_COLOR` varchar(45) NOT NULL,
  `TICK_LABEL_COLOR` varchar(45) NOT NULL,
  `TICK_MARK_COLOR` varchar(45) NOT NULL,
  `POSITION` int(11) NOT NULL,
  `AUTO_RANGE` tinyint(1) NOT NULL,
  `AUTO_RANGE_INCL_ZERO` tinyint(1) NOT NULL,
  `AUTO_RANGE_MARGIN` double NOT NULL,
  `LOWER_BOUND` double NOT NULL,
  `UPPER_BOUND` double NOT NULL,
  `AUTO_TICK_UNITS` tinyint(1) NOT NULL,
  `TICK_UNIT` double NOT NULL,
  `GRID_UNIT` double NOT NULL,
  `DEFAULT_SUBPLOT` int(11) NOT NULL,
  PRIMARY KEY  (`ndx`)
);

DROP TABLE IF EXISTS `ctg_pens`;
CREATE TABLE  `ctg_pens` (
  `PointID` varchar(255) NOT NULL default '',
  `NAME` varchar(255) default NULL,
  `LOCATION` varchar(255) NOT NULL,
  `TYPE` varchar(100) NOT NULL,
  `COL_NAME` varchar(100) default NULL,
  `TABLE_NAME` varchar(100) default NULL,
  `XVAL_COL_NAME` varchar(60) default NULL,
  `TAG_PATH` varchar(255) default NULL,
  `AGGREGATION_MODE` varchar(45) default NULL,
  `AXIS` varchar(45) default NULL,
  `SUBPLOT` int(11) default '0',
  `ENABLED` tinyint(1) NOT NULL default '1',
  `DATASOURCE` varchar(45) default NULL,
  `COLOR` varchar(45) default NULL,
  `DASH_PATTERN` varchar(45) default NULL,
  `RENDER_STYLE` int(10) unsigned default '1',
  `LINE_WEIGHT` int(10) unsigned default '1',
  `SHAPE` int(10) unsigned default '0',
  `FILL_SHAPE` tinyint(1) NOT NULL default '1',
  `GROUP_NAME` varchar(45) default NULL,
  `WHERE_CLAUSE` varchar(155) default NULL,
  `DIGITAL` tinyint(1) NOT NULL default '0',
  `OVERRIDE_AUTOCOLOR` tinyint(1) NOT NULL default '0',
  `HIDDEN` tinyint(1) NOT NULL default '0',
  PRIMARY KEY  (`PointID`)
);

DROP TABLE IF EXISTS `ctg_saved_graph_pens`;
CREATE TABLE  `ctg_saved_graph_pens` (
  `SavedGraphID` int(11) NOT NULL auto_increment,
  `PointID` varchar(255) NOT NULL,
  PRIMARY KEY  USING BTREE (`SavedGraphID`,`PointID`)
);

DROP TABLE IF EXISTS `ctg_saved_graphs`;
CREATE TABLE  `ctg_saved_graphs` (
  `ID` int(11) NOT NULL auto_increment,
  `Name` varchar(255) NOT NULL,
  `Description` varchar(255) NOT NULL,
  PRIMARY KEY  (`ID`)
);

DROP TABLE IF EXISTS `ctg_subplots`;
CREATE TABLE  `ctg_subplots` (
  `ID` int(11) NOT NULL,
  `WEIGHT` int(11) NOT NULL,
  `OVERRIDE_BACKGROUND` tinyint(1) NOT NULL,
  `OVERRIDE_BACKGROUND_COLOR` varchar(45) NOT NULL,
  PRIMARY KEY  (`ID`)
);
