drop database if exists SO;
CREATE database IF NOT EXISTS SO DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

use SO;

CREATE TABLE posts (
  Id INT NOT NULL PRIMARY KEY, 
  PostTypeId SMALLINT, 
  AcceptedAnswerId INT, 
  CreationDate DATETIME, 
  Score INT NULL, 
  ViewCount INT NULL, 
  Body text NULL, 
  OwnerUserId INT, 
  LastEditorUserId INT, 
  LastEditDate DATETIME, 
  LastActivityDate DATETIME, 
  Title varchar(256), 
  Tags VARCHAR(256), 
  AnswerCount INT, 
  CommentCount INT, 
  FavoriteCount INT, 
  CommunityOwnedDate DATETIME, 
  ParentId INT
);

load xml local infile '/data/Posts.xml' into table posts rows identified by '<row>';

SELECT 'Id','Tags', 'Body'
UNION ALL
SELECT Id, Tags, #replace(replace(Tags,'<','' ), '>' , '') 
 replace(Body,',',' ') # SUBSTRING(Body FROM POSITION('<code>' IN Body) FOR (POSITION('</code>' IN Body) - POSITION('<code>' IN Body)))
   from (
select Id, Tags, Body from Posts  WHERE Body like '%<code> _%_%_%_%_%_%_%_%_ </code>%' and Score>0 and Tags is not null 
) a 
    INTO OUTFILE '/data/data_raw.csv' FIELDS
TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n';


SET net_read_timeout=600;

