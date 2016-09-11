# -*- coding: utf-8 -*-
import sys,os
import unittest

# ../libをロードパスに入れる
app_home = os.path.join( os.path.dirname(os.path.abspath(__file__)) , ".." )
sys.path.append(os.path.join(app_home,"lib"))

# ../テスト対象のライブラリのロード
from my_lib import MyLib

class TestMyLib(unittest.TestCase):

    def test_get_name(self):
        ml = MyLib()
        self.assertEqual(ml.get_name(), "my_lib")

if __name__ == '__main__':
    unittest.main()
