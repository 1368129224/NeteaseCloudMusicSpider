show databases like '163music';
drop database if exists 163music;
create DATABASE 163music;

CREATE TABLE T_Tag(
    PID BIGINT    COMMENT '歌单ID' ,
    tag VARCHAR(32)    COMMENT '标签' 
) COMMENT = '标签表 ';/*SQL@Run*/

CREATE TABLE T_SongName(
    SID BIGINT    COMMENT '歌曲ID' ,
    SNAME VARCHAR(1024)    COMMENT '歌曲名' 
) COMMENT = '歌名表 ';/*SQL@Run*/

CREATE TABLE T_Huayu(
    PID BIGINT NOT NULL   COMMENT '歌单ID' ,
    NAME VARCHAR(128)    COMMENT '歌单名' ,
    USERID INT    COMMENT '创建者ID' ,
    SUBSCRIBEDCOUNT INT    COMMENT '收藏数' ,
    TRACKCOUNT INT    COMMENT '歌曲数' ,
    PLAYCOUNT INT    COMMENT '播放数' ,
    SHARECOUNT INT    COMMENT '分享数' ,
    COMMENTCOUNT INT    COMMENT '评论数' ,
    PRIMARY KEY (PID)
) COMMENT = '华语歌单表';/*SQL@Run*/

CREATE TABLE T_HuayuSong(
    PID BIGINT    COMMENT '歌单ID' ,
    SID BIGINT    COMMENT '歌曲ID' ,
    SNAME VARCHAR(1024)    COMMENT '歌曲名' 
) COMMENT = '华语歌单歌曲表 ';/*SQL@Run*/