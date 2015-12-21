from tables import *
import h5py
import sys
import os
import rlcompleter, readline
import Crypt
VERSION = 0.2

class SimpleCompleter(object):

    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            # This is the first time for this text, so build a match list.
            if text:
                self.matches = [s
                                for s in self.options
                                if s and s.startswith(text)
                                ]
            else:
                self.matches = self.options[:]

        # Return the state'th item from the match list,
        # if we have that many.
        try:
            response = self.matches[state]
        except IndexError:
            response = None
        return response
def create(title):
    h5file = open_file("{0}.h5".format(title), mode = "w", title=str(title))
    h5file.close()

def dbls():
    list = os.popen("ls *.h5 2> /dev/null").read()
    return list
def GenKey(id):
    Crypt.key(id)

def keyls():
    list = os.popen("ls *.h5k 2> /dev/null").read()
    return list
def ksls():
    list = os.popen("ls *.h5ks 2> /dev/null").read()
    return list

def group(id,tab,db):
    try:
        dblist = dbls()
        if db in dblist:
            h5file = open_file("{0}.h5".format(db), mode = "r+", title=str(db))
        if db not in dblist:
            print "Please run: CREATE DB {0}".format(db)
            return
        group = h5file.create_group("/", '{0}'.format(id), '{0}'.format(id))
        class cbd(IsDescription):
            key = StringCol(8094)
            id = StringCol(8094)
        tbl = []
        ctable = range(0,256)
        table = h5file.create_table(group, tab, cbd, "H5QL TBL: {}".format(tab))
        entry = table.row
        print entry
        h5file.close()
    except NaturalNameWarning:
        pass

def display(db):
    dblist = dbls()
    try:
        if db in dblist:
            h5file = open_file("{0}.h5".format(db), mode = "r", title=str(db))
        if db not in dblist:
            print "Please run: CREATE DB {0}".format(db)
            return
        print(h5file)
        h5file.close()
    except IOError:
        print "Error: DB Doesn't exist"

def termcount(term):
    g = z.index(term)
    return g
if __name__ == '__main__':
    rl = SimpleCompleter(['CREATE',
                          'DISPLAY',
                          'SET',
                          'GET',
                          'DELETE',
                          'CLOSE',
                          'SYNC',
                          'ABOUT',
                          'LIST',
                          'ALGO'])
    readline.set_completer(rl.complete)
    try:
        readline.parse_and_bind('tab: complete')
        import tables
        while 1:
            x = raw_input("> ")
            if "#H5QL" in x:
                print "Scripting interface: Strarted"
                x = raw_input("")
            if "#EOF" in x:
                print "Scripting interface: Stopped"
                exit()
            if ";" in x:
                pass
            z = x.split()
            if "ALGO" in z:
                a = Crypt.info()
                print "Algorithm: {}".format(a)
            if "CREATE" in z:
                if "DB" in z[1]:
                    try:
                        g = termcount("DB")
                        t = z[g+1]
                        create(t)
                        print "H5QL DB: {}.h5".format(t)
                    except IndexError:
                        print "ERROR"
                        pass
                    except NaturalNameWarning:
                        pass
                elif "KEY" == z[1]:
                    i = termcount("KEY")
                    t = z[i+1]
                    Crypt.key(t)
                    print "H5QL Key: {}.h5k".format(t)
                elif "GROUP" in z:
                    try:
                        i = termcount("DB")
                        t = z[i+1]
                        h = termcount("ID")
                        v = z[h+1]
                        j = termcount("TBL")
                        y = z[j+1]
                        group(v,y,db=t)
                    except IndexError:
                        print "ERROR: Input Error"
                        pass
                    except tables.exceptions.NodeError:
                        print "ERROR: Child Exist"
                        pass
                    except ValueError:
                        print "Error: Value Error"
                        pass
                    except NaturalNameWarning:
                        pass
                if "KEYSTORE" == z[1]:
                    if "KEY" in z:
                        a = termcount("KEY")
                        y = z[a+1]
                        b = termcount("STORE")
                        x = z[b+1]
                        Crypt.keychain(y,x)
            if "DISPLAY" in z:
                if "DB" in z:
                    try:
                        x = termcount("DB")
                        t = z[x+1]
                        display(t)
                    except IndexError:
                        print "Error: Input Error"
                        pass
                    except ValueError:
                        print "Error: Value Error"
                        pass
                    except NaturalNameWarning:
                        pass
            if "SET" in z:
                if "DB" in z:
                    try:
                        import h5py
                        g = termcount("DB")
                        t = z[g+1]
                        h = termcount("ID")
                        v = z[h+1]
                        d = termcount("DATA")
                        y = z[d+1]
                        f = termcount("KEY")
                        x = z[f+1]
                        data = Crypt.encrypt(y,x)
                        f = h5py.File('{0}.h5'.format(t),'r+')
                        u = f.attrs.create(name='{0}'.format(v),data=data)
                        s = f.attrs.get(name='{0}'.format(v))
                        print "[{0}: {1}]".format(v,s)
                    except ValueError:
                        print "Error"
                        pass
                    except IndexError:
                        print "Error"
                        pass
                    except NaturalNameWarning:
                        pass
            if "GET" in z:
                if "DB" in z:
                    try:
                        import h5py
                        g = termcount("DB")
                        t = z[g+1]
                        h = termcount("ID")
                        v = z[h+1]
                        i = termcount("KEY")
                        x = z[i+1]
                        f = h5py.File('{0}.h5'.format(t),'r+')
                        s = f.attrs.get(name='{0}'.format(v))
                        blob = Crypt.decrypt(s,x)
                        print "[{0}: {1}]".format(v,blob)
                    except ValueError:
                        print "Error"
                        pass
                    except IndexError:
                        print "Error"
                        pass
                    except NaturalNameWarning:
                        pass
                    except TypeError:
                        print "Error: No data found"
                        pass
            if "LIST" in z:
                if "DB" in z:
                    z = dbls()
                    t = z.split()
                    for i in t:
                        print "{1} : {0}".format(i.rstrip(".h5"),t.index(i))
                elif "KEY" in z:
                    z = keyls()
                    t = z.split()
                    for i in t:
                        print "{1} : {0}".format(i.rstrip(".h5k"),t.index(i))
                elif "KEYSTORE" in z:
                    z = ksls()
                    t = z.split()
                    for i in t:
                        print "{1} : {0} ".format(i.rstrip(".h5ks"),t.index(i))
            if "DELETE" in z:
                if "DB" in z:
                    try:
                        g = termcount("DB")
                        t = z[g+1]
                        os.popen("rm {0}.h5".format(t)).read()
                        print "Deleted DB: {0}".format(t)
                    except IndexError:
                        print "Error"
                        pass
                    except NaturalNameWarning:
                        pass
                elif "KEY" in z:
                    g = termcount("KEY")
                    t = z[g+1]
                    os.popen("rm {0}.h5k".format(t)).read()
                    print "Deleted Key: {0}".format(t)
                elif "KEYSTORE" in z:
                    g = termcount("KEYSTORE")
                    t = z[g+1]
                    os.popen("rm {0}.h5ks".format(t)).read()
                    print "Deleted Keystore: {0}".format(t)
            if "CLOSE" in z:
                if "DB" in z:
                    try:
                        g = termcount("DB")
                        t = z[g+1]
                        h5file = open_file("{0}.h5".format(t), mode = "r", title=str(t))
                        h5file.close()
                    except IndexError:
                        print "Error"
                        pass
                    except ValueError:
                        print "Error: IO Error"
                        pass
                    except NaturalNameWarning:
                        pass
            if "DATASET" in z:
                if "DB" in z:
                    g = termcount("DB")
                    a = z[g+1]
                    h = termcount("ID")
                    b = z[h+1]
                    j = termcount("DATA")
                    c = z[j+1]
                    f = h5py.File('{0}.h5'.format(a),'r+')
                    f.create_dataset(name=b,data=c)
            if "LINK" in z:
                if " DB" in z:
                    g = termcount("DB")
                    a = z[g+1]
                    h = termcount("ID")
                    b = z[h+1]
                    i = termcount("SRC-TBL")
                    c = z[i+1]
                    k = termcount("DST-TBL")
                    d = z[k+i]
                    f = open_file('{0}.h5'.format(a),'r+')
                    l = f.create_hard_link(b,str(c),str(d),createparents=True)
                    print l
            if "SYNC" in z:
                os.popen("sync").read()
                print "Syncing"
            if "EXIT" in z:
                print "Saving Environment"
                sys.exit()
            if "ABOUT" in z:
                readline.set_completer(SimpleCompleter(['HQL']).complete)
                if "HQL" in z:
                    print "Version: {}".format(VERSION)
                    print "Backend: HDF5"
    except KeyboardInterrupt:
        exit()
    except EOFError:
        pass
    except NaturalNameWarning:
        pass