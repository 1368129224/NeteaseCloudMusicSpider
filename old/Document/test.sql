show databases like '163music';
drop database if exists 163music;
create DATABASE 163music;

CREATE TABLE T_Tag(
    PID BIGINT    COMMENT '�赥ID' ,
    tag VARCHAR(32)    COMMENT '��ǩ' 
) COMMENT = '��ǩ�� ';/*SQL@Run*/

CREATE TABLE T_SongName(
    SID BIGINT    COMMENT '����ID' ,
    SNAME VARCHAR(1024)    COMMENT '������' 
) COMMENT = '������ ';/*SQL@Run*/

CREATE TABLE T_Huayu(
    PID BIGINT NOT NULL   COMMENT '�赥ID' ,
    NAME VARCHAR(128)    COMMENT '�赥��' ,
    USERID INT    COMMENT '������ID' ,
    SUBSCRIBEDCOUNT INT    COMMENT '�ղ���' ,
    TRACKCOUNT INT    COMMENT '������' ,
    PLAYCOUNT INT    COMMENT '������' ,
    SHARECOUNT INT    COMMENT '������' ,
    COMMENTCOUNT INT    COMMENT '������' ,
    PRIMARY KEY (PID)
) COMMENT = '����赥��';/*SQL@Run*/

CREATE TABLE T_HuayuSong(
    PID BIGINT    COMMENT '�赥ID' ,
    SID BIGINT    COMMENT '����ID' ,
    SNAME VARCHAR(1024)    COMMENT '������' 
) COMMENT = '����赥������ ';/*SQL@Run*/