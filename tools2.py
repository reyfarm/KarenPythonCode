from itoolkit import *
from itoolkit.transport import DatabaseTransport
import ibm_db_dbi

itool = iToolKit()

conn = ibm_db_dbi.connect()
itransport = DatabaseTransport(conn)

itool.add(iCmd('addlible', 'ADDLIBLE TOOLBOX'))

itool.add(
iPgm('pypgm001c', 'PYPGM001C')
.addParm(iData('RTNMSG', '50a', 'a'))
.addParm(iData('AMOUNT', '15p2', '33.33'))
)

itool.add(
iPgm('programcheck', '#PGMCHK')
.addParm(iData('PROGRAM', '10a', 'ORDDIR'))
.addParm(iData('RUNNING', '1a', 'N'))
)

itool.call(itransport)

programcheck = itool.dict_out('programcheck')

if 'success' in programcheck:
    print(programcheck['success'])
    print("Return parameter values:")
    print("PROGRAM: " + programcheck['PROGRAM'])
    print("RUNNING: " + programcheck['RUNNING'])
else:
    raise Exception("Program call error:" + programcheck['error'])