import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))

from qhost import Parser

class TestParser(unittest.TestCase):
    def setUp(self):
        self.one_xml = "<Data><Node><name>n061</name><state>job-exclusive</state><np>8</np><properties>compute,enc4</properties><ntype>cluster</ntype><jobs>0/1158769.fortytwo.ibest.uidaho.edu, 1/1158769.fortytwo.ibest.uidaho.edu, 2/1158769.fortytwo.ibest.uidaho.edu, 3/1158769.fortytwo.ibest.uidaho.edu, 4/1158769.fortytwo.ibest.uidaho.edu, 5/1158769.fortytwo.ibest.uidaho.edu, 6/1158769.fortytwo.ibest.uidaho.edu, 7/1158769.fortytwo.ibest.uidaho.edu</jobs><status>rectime=1390343608,varattr=,jobs=1158769.fortytwo.ibest.uidaho.edu,state=free,netload=1173275966756391,gres=,loadave=8.02,ncpus=8,physmem=32941056kb,availmem=33140804kb,totmem=35038200kb,idletime=14954471,nusers=1,nsessions=1,sessions=17922,uname=Linux n061.fortytwo.ibest.uidaho.edu 2.6.32-279.14.1.el6.x86_64 #1 SMP Tue Nov 6 23:43:09 UTC 2012 x86_64,opsys=linux</status><gpus>0</gpus></Node></Data>"
        self.two_xml = "<Data><Node><name>n061</name><state>job-exclusive</state><np>8</np><properties>compute,enc4</properties><ntype>cluster</ntype><jobs>0/1158769.fortytwo.ibest.uidaho.edu, 1/1158769.fortytwo.ibest.uidaho.edu, 2/1158769.fortytwo.ibest.uidaho.edu, 3/1158769.fortytwo.ibest.uidaho.edu, 4/1158769.fortytwo.ibest.uidaho.edu, 5/1158769.fortytwo.ibest.uidaho.edu, 6/1158769.fortytwo.ibest.uidaho.edu, 7/1158769.fortytwo.ibest.uidaho.edu</jobs><status>rectime=1390343608,varattr=,jobs=1158769.fortytwo.ibest.uidaho.edu,state=free,netload=1173275966756391,gres=,loadave=8.02,ncpus=8,physmem=32941056kb,availmem=33140804kb,totmem=35038200kb,idletime=14954471,nusers=1,nsessions=1,sessions=17922,uname=Linux n061.fortytwo.ibest.uidaho.edu 2.6.32-279.14.1.el6.x86_64 #1 SMP Tue Nov 6 23:43:09 UTC 2012 x86_64,opsys=linux</status><gpus>0</gpus></Node><Node><name>n062</name><state>job-exclusive</state><np>8</np><properties>compute,enc4</properties><ntype>cluster</ntype><jobs>0/1158769.fortytwo.ibest.uidaho.edu, 1/1158769.fortytwo.ibest.uidaho.edu, 2/1158769.fortytwo.ibest.uidaho.edu, 3/1158769.fortytwo.ibest.uidaho.edu, 4/1158769.fortytwo.ibest.uidaho.edu, 5/1158769.fortytwo.ibest.uidaho.edu, 6/1158769.fortytwo.ibest.uidaho.edu, 7/1158769.fortytwo.ibest.uidaho.edu</jobs><status>rectime=1390343641,varattr=,jobs=1158769.fortytwo.ibest.uidaho.edu,state=free,netload=839087609111363,gres=,loadave=8.05,ncpus=8,physmem=32941056kb,availmem=33157168kb,totmem=35038200kb,idletime=14954507,nusers=1,nsessions=1,sessions=8739,uname=Linux n062.fortytwo.ibest.uidaho.edu 2.6.32-279.14.1.el6.x86_64 #1 SMP Tue Nov 6 23:43:09 UTC 2012 x86_64,opsys=linux</status><gpus>0</gpus></Node></Data>"
        self.unknowns_xml = "<Data><Node><name>n001</name><state>offline</state><np>8</np><properties>compute,enc1</properties><ntype>cluster</ntype><status>rectime=1390362976,varattr=,jobs=,state=free,netload=18838668091,gres=,loadave=0.22,ncpus=8,physmem=32941056kb,availmem=33343196kb,totmem=35038200kb,idletime=972119,nusers=0,nsessions=? 0,sessions=? 0,uname=Linux n001.fortytwo.ibest.uidaho.edu 2.6.32-279.14.1.el6.x86_64 #1 SMP Tue Nov 6 23:43:09 UTC 2012 x86_64,opsys=linux</status><gpus>0</gpus></Node></Data>"
    def test_parse_one(self):
        p = Parser(self.one_xml)
        nlist = p.parse()
        n = nlist[0]

        self.assertEqual(n.name, 'n061')
        self.assertEqual(n.procs, 8)
        self.assertEqual(n.uname, u'Linux n061.fortytwo.ibest.uidaho.edu 2.6.32-279.14.1.el6.x86_64 #1 SMP Tue Nov 6 23:43:09 UTC 2012 x86_64')
        self.assertEqual(n.os, u'linux')
        self.assertEqual(n.state, u'job-exclusive')
        self.assertEqual(n.sessions, 17922)
        self.assertEqual(n.nsessions, 1)
        self.assertEqual(n.nusers, 1)
        self.assertEqual(n.physmem, 32941056)
        self.assertEqual(n.totmem, 35038200)
        self.assertEqual(n.availmem, 33140804)
        self.assertEqual(len(n.jobs), 8)
        self.assertTrue('0/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('1/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('2/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('3/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('4/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('5/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('6/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('7/1158769.fortytwo.ibest.uidaho.edu', n.jobs)

    def test_parse_multi(self):
        p = Parser(self.two_xml)
        nlist = p.parse()

        n = nlist[0]
        self.assertEqual(n.name, 'n061')
        self.assertEqual(n.procs, 8)
        self.assertEqual(n.uname, u'Linux n061.fortytwo.ibest.uidaho.edu 2.6.32-279.14.1.el6.x86_64 #1 SMP Tue Nov 6 23:43:09 UTC 2012 x86_64')
        self.assertEqual(n.os, u'linux')
        self.assertEqual(n.state, u'job-exclusive')
        self.assertEqual(n.sessions, 17922)
        self.assertEqual(n.nsessions, 1)
        self.assertEqual(n.nusers, 1)
        self.assertEqual(n.physmem, 32941056)
        self.assertEqual(n.totmem, 35038200)
        self.assertEqual(n.availmem, 33140804)
        self.assertEqual(len(n.jobs), 8)
        self.assertTrue('0/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('1/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('2/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('3/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('4/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('5/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('6/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('7/1158769.fortytwo.ibest.uidaho.edu', n.jobs)

        n = nlist[1]
        self.assertEqual(n.name, 'n062')
        self.assertEqual(n.procs, 8)
        self.assertEqual(n.uname, u'Linux n062.fortytwo.ibest.uidaho.edu 2.6.32-279.14.1.el6.x86_64 #1 SMP Tue Nov 6 23:43:09 UTC 2012 x86_64')
        self.assertEqual(n.os, u'linux')
        self.assertEqual(n.state, u'job-exclusive')
        self.assertEqual(n.sessions, 8739)
        self.assertEqual(n.nsessions, 1)
        self.assertEqual(n.nusers, 1)
        self.assertEqual(n.physmem, 32941056)
        self.assertEqual(n.totmem, 35038200)
        self.assertEqual(n.availmem, 33157168)
        self.assertEqual(len(n.jobs), 8)
        self.assertTrue('0/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('1/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('2/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('3/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('4/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('5/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('6/1158769.fortytwo.ibest.uidaho.edu', n.jobs)
        self.assertTrue('7/1158769.fortytwo.ibest.uidaho.edu', n.jobs)

    def test_for_unknowns(self):
        p = Parser(self.unknowns_xml)
        nlist = p.parse()

        n = nlist[0]
        self.assertEqual(n.sessions, 0)
        self.assertEqual(n.nsessions, 0)

if __name__ == '__main__':
    unittest.main()
