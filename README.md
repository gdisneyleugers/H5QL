# H5QL
HDF5 Query Language 
To run:
==
tail -f |./h5ql dba.h5ql
To start scripting interface"
#H5QL
==
To delete DB:
DELETE DB db0 ;
==
To delete Key:
DELETE KEY db0 ; 
==
To delete Keystore:
DELETE KEYSTORE db0 ;
==
To create DB:
CREATE DB db0 ;
==
To create key: 
CREATE KEY db0 ;
==
To create keystore:
CREATE KEYSTORE STORE db0 KEY db0 ;
== 
To create group and table:
CREATE GROUP DB db0 ID login TBL login ; 
==
To set table data:
SET DB db0 ID login DATA admin KEY dba ;
==
To display DB:
DISPLAY DB db0 ;
==
To get table data:
GET DB db0 ID login KEY dba ;
==
To list DB's:
LIST DB ;
==
To list Key's:
LIST KEY ;
==
To list keystore:
LIST KEYSTORE ;
==
To stop scripting interface:
#EOF
