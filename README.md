# H5QL
HDF5 Query Language 
tail -f |./h5ql dba.h5ql
====================================
Running:  #H5QL

 Scripting interface: Strarted
====================================
Running:  DELETE DB db0 ; SYNC ;

 Deleted DB: db0
Syncing

 ====================================
Running:  DELETE KEY db0 ; SYNC ;

 Deleted Key: db0
Syncing

 ====================================
Running:  DELETE KEYSTORE db0 ; SYNC ;

 Deleted Keystore: db0
Syncing

 ====================================
Running:  CREATE DB db0 ; SYNC ;

 H5QL DB: db0.h5
Syncing

 ====================================
Running:  CREATE KEY db0 ; SYNC ;

 H5QL Key: db0.h5k
Syncing

 ====================================
Running:  CREATE KEY dba ; SYNC ;

 H5QL Key: dba.h5k
Syncing

 ====================================
Running:  CREATE KEYSTORE STORE db0 KEY db0 ;

 Keystore: db0.h5ks
Pass: $2b$12$MifGfgzncXaGWXPDTAKpau18a6xk/23QE6DwH.1zteiyi/yWbEAHq

 ====================================
Running:  CREATE GROUP DB db0 ID login TBL login ; SYNC ;

 /login/login.row (Row), pointing to row #0
Syncing

 ====================================
Running:  SET DB db0 ID login DATA admin KEY dba ; SYNC ;

 [login: Qm+pwUf62z67VwS/le68yL96oZJ4NS1vkfgYPWA7Icg=]
Syncing

 ====================================
Running:  CREATE GROUP DB db0 ID password TBL password ; SYNC ;

 /password/password.row (Row), pointing to row #0
Syncing

 ====================================
Running:  SET DB db0 ID password DATA password KEY dba ; SYNC ;

 [password: DmjVr1tSa/Q3gK5sV1kVo796oZJ4NS1vkfgYPWA7Icg=]
Syncing

 ====================================
Running:  CREATE GROUP DB db0 ID servers TBL servers ; SYNC ;

 /servers/servers.row (Row), pointing to row #0
Syncing

 ====================================
Running:  CREATE GROUP DB db0 ID server TBL server ; SYNC ;

 /server/server.row (Row), pointing to row #0
Syncing

 ====================================
Running:  SET DB db0 ID servers DATA localhost KEY db0 ; SYNC ;

 [servers: QMqKHamvoYdPeT6f/m/IVjRoU5t10EPZrUBZZpui/EE=]
Syncing

 ====================================
Running:  SET DB db0 ID server DATA 127.0.0.1 KEY db0 ; SYNC ;

 [server: aU4WI0L5YlpOds2pZht13zRoU5t10EPZrUBZZpui/EE=]
Syncing

 ====================================
Running:  DISPLAY DB db0 ; SYNC ;

 db0.h5 (File) 'db0'
Last modif.: 'Sun Dec 20 20:51:11 2015'
Object Tree: 
/ (RootGroup) 'db0'
/login (Group) 'login'
/login/login (Table(0,)) 'H5QL TBL: login'
/password (Group) 'password'
/password/password (Table(0,)) 'H5QL TBL: password'
/server (Group) 'server'
/server/server (Table(0,)) 'H5QL TBL: server'
/servers (Group) 'servers'
/servers/servers (Table(0,)) 'H5QL TBL: servers'

Syncing

 ====================================
Running:  GET DB db0 ID login KEY dba ;

 [login: admin]

 ====================================
Running:  GET DB db0 ID password KEY dba ;

 [password: password]

 ====================================
Running:  GET DB db0 ID servers KEY db0 ;

 [servers: localhost]

 ====================================
Running:  GET DB db0 ID server KEY db0 ;

 [server: 127.0.0.1]

 ====================================
Running:  LIST DB ;

 0 : db0

 ====================================
Running:  LIST KEY ;

 0 : db0
1 : dba

 ====================================
Running:  LIST KEYSTORE ;

 0 : db0 

 ====================================
Running:  #EOF

 Scripting interface: Stopped
====================================
H5QL Scripting Interface
 Version: 0.2
Backend: HDF5
 Algorithm: AES-192
 
====================================
