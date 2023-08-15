-- Take first argument from cmd and use it to list all table of database
SET @db_name = CONVERT(@@mysql_cli_opt_dB, CHAR);
USE @db_name;
SHOW TABLES;
