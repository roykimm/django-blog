from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# 테스트 방식은 실제 데이터베이스는 건드리지 않고
# 가상의 데이터 베이스를 새로 만들어 테스트 한다.


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        #self.assertEqual(2, 2)

        # 1.1 포스트 목록 페이지를 가져온다.
        response = self.client.get('/myblog/')
        # 1.2 정상적으로 페이지가 로드된다.
        self.assertEqual(response.status_code, 200)
        # 1.3 페이지 타이틀은 'BLOG'이다.
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog')
        # 1.4 네비게이션 바가 있다.
        navbar = soup.nav
        # 1.5 Blog, About Me 라는 문구가 네비게이션 바에 있다.
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        # 2.1 메인영역에 게시물이 하나도 없다면
        self.assertEqual(Post.Objects.count(), 0)
        # 2.2 아직 게시물이 없습니다.  라는 문구가 보인다.
        main_area = soup.find('div', id="main-area")
        self.assertIn('아직 게시물이 없습니다.', main_area.text)
        # 3.1 게시물이 2개 있다면
        post_001 = Post.objects.create(
            title='첫번째 포스트입니다.',
            content='Hello world/dfdfdfdf'
        )
        post_002 = Post.objects.create(
            title='두번째 포스트입니다.',
            content='Hello ㅇㄹㅇㄹㄹㅇworld/dfdfdfdf'
        )
        self.assertEqual(Post.objects.count(), 2)

        # 3.2 포스트 목록 페이지를 새로고침 했을때
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)
        # 3.3 메인영역에 포스트2개의 타이틀이 존재한다.
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)
        # 3.4 '아직 게시물이 없습니다.'라는 문구는 더 이상 보이지 않는다.
        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)

    def test_post_detail(Self):
        # 1.1 포스트가 하나 있다.
        # 1.2 그 포스트의 url은 '/blog/1/' 이다
        pass
