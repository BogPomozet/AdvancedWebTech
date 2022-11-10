import unittest
import Testing

class TestingTest (unittest.TestCase):
    def test_root(self):
        self.app=Testing.app.test_client()
        out=self.app.get('/')
        assert '200 OK' in out.content_type
        assert 'charset=utf-8' in out.content_type
        assert 'text/html' in out.content_type

if __name__=="__main__":
    unittest.main()