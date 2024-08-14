from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from wagtail.blocks import PageChooserBlock
from wagtail.snippets.models import register_snippet


class ImageSliderBlock(blocks.StructBlock):
    images = blocks.ListBlock(
        ImageChooserBlock(),
        label="Slider Images"
    )

    class Meta:
        template = "home/blocks/image_slider_block.html"
        icon = "image"
        label = "Image Slider"


class VisionBlock(blocks.StructBlock):
    text = blocks.TextBlock(label="Vision Text")
    image = ImageChooserBlock(label="Vision Image")

    class Meta:
        template = "home/blocks/vision_block.html"
        icon = "doc-full"
        label = "Vision Section"


class LatestNewsBlock(blocks.StructBlock):
    news = blocks.ListBlock(
        PageChooserBlock(target_model='home.NewsPage'),
        label="Latest News"
    )

    class Meta:
        template = "home/blocks/latest_news_block.html"
        icon = "list-ul"
        label = "Latest News"


class HomePage(Page):
    body = StreamField([
        ('image_slider', ImageSliderBlock()),
        ('vision_section', VisionBlock()),
        ('latest_news', LatestNewsBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    class Meta:
        verbose_name = "Home Page"


class NewsPage(Page):
    date = models.DateField("Post date")
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['news_pages'] = self.get_siblings().live().order_by('-date')
        return context

    class Meta:
        verbose_name = "News Page"