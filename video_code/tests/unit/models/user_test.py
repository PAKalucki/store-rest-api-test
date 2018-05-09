from video_code.models.user import UserModel
from video_code.tests.base import BaseTest


class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test',
                         "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user.password, 'abcd',
                         "The password of the user after creation does not equal the constructor argument.")
