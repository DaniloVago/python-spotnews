from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from tests.utils.date_converter import date_converter
from news.models import Category, News, User
from bs4 import BeautifulSoup
import pytest


@pytest.mark.dependency(scope="class")
class NewsDetailTemplateTest(TestCase):
    def setUp(self):
        User.objects.create(
            name="Yarpen Zigrin",
            email="yarpen.zigrin@gmail.com",
            password="123456",
            role="user",
        )
        category = Category.objects.create(name="Tecnologia")
        self.news = News.objects.create(
            title="Test title",
            content="Test content",
            author=User.objects.get(name="Yarpen Zigrin"),
            created_at="2023-08-08",
            image="image.jpg",
        )
        self.news.categories.add(category)
        self.response = self.client.get(
            reverse("news-details-page", args=[self.news.id])
        )
        self.soup = BeautifulSoup(self.response.content, "html.parser")

    def test_news_detail_template_rendering(self):
        self.assertTemplateUsed(self.response, "news_details.html")

    def test_news_detail_template_title_block(self):
        self.assertContains(
            self.response,
            "<title> Página de Detalhes da Notícia </title>",
            html=True,
        )

    def test_news_details_template_header_block(self):
        header = self.soup.find("header")
        self.assertTrue(header)
        self.assertEqual(header.get("class")[0], "header")

        self.assertTrue(header.ul)
        self.assertEqual(header.ul.get("class")[0], "header-links")

    def test_news_detail_title(self):
        title = self.soup.find("h1")

        self.assertTrue(title)
        self.assertEqual(title.get("class")[0], "news-title")
        self.assertTrue("Test title" in title.text)

    def test_news_detail_content(self):
        content = self.soup.find("p")

        self.assertTrue(content)
        self.assertEqual(content.get("class")[0], "news-content")
        self.assertTrue("Test content" in content.text)

    def test_news_detail_categories(self):
        categories = self.soup.find_all("span", {"class": "news-categories"})

        self.assertTrue(categories)
        self.assertTrue("Tecnologia" in categories[0].text)

    def test_news_detail_author(self):
        author = self.soup.find("span", {"class": "news-author"})

        self.assertTrue(author)
        self.assertEqual(author.get("class")[0], "news-author")
        self.assertTrue("Yarpen Zigrin" in author.text)

    def test_news_detail_image(self):
        image = self.soup.find("img")

        self.assertTrue(image)
        self.assertEqual(image.get("src"), f"{settings.STATIC_URL}image.jpg")

    def test_news_detail_date_format(self):
        formatted_date = date_converter(self.news.created_at)
        self.assertIn(
            f"{formatted_date}",
            self.response.content.decode(),
        )

    def test_home_page_news_links(self):
        ul = self.soup.find("ul", {"class": "header-links"})
        self.assertTrue(ul)
        self.assertTrue(ul.a)
        self.assertEqual(ul.a.get("href"), reverse("home-page"))
        self.assertEqual(ul.a.text, "Home")

    @pytest.mark.dependency(
        depends=[
            "NewsDetailTemplateTest::test_news_detail_template_rendering",
            "NewsDetailTemplateTest::test_news_detail_template_title_block",
            "NewsDetailTemplateTest::test_news_details_template_header_block",
            "NewsDetailTemplateTest::test_news_detail_title",
            "NewsDetailTemplateTest::test_news_detail_content",
            "NewsDetailTemplateTest::test_news_detail_categories",
            "NewsDetailTemplateTest::test_news_detail_author",
            "NewsDetailTemplateTest::test_news_detail_image",
            "NewsDetailTemplateTest::test_news_detail_date_format",
            "NewsDetailTemplateTest::test_home_page_news_links",
        ]
    )
    def test_validate_final_news_details_template(self):
        pass
