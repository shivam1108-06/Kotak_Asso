from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ('', 'Select a service'),
        ('virtual_cfo', 'Virtual CFO Services'),
        ('tax_planning', 'Tax Planning & Compliance'),
        ('business_advisory', 'Business Advisory'),
        ('accounting', 'Accounting & Bookkeeping'),
        ('audit', 'Audit & Assurance'),
        ('gst', 'GST Compliance'),
        ('company_formation', 'Company Formation'),
        ('other', 'Other'),
    ]

    BUDGET_CHOICES = [
        ('', 'Select budget range'),
        ('below_25k', 'Below 25,000/month'),
        ('25k_50k', '25,000 - 50,000/month'),
        ('50k_1l', '50,000 - 1,00,000/month'),
        ('above_1l', 'Above 1,00,000/month'),
        ('discuss', 'Prefer to discuss'),
    ]

    URGENCY_CHOICES = [
        ('', 'Select timeline'),
        ('immediate', 'Immediate (Within a week)'),
        ('short', 'Short-term (1-2 months)'),
        ('medium', 'Medium-term (3-6 months)'),
        ('flexible', 'Flexible / No rush'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    service_interested = models.CharField(max_length=50, choices=SERVICE_CHOICES, blank=True)
    budget_range = models.CharField(max_length=30, choices=BUDGET_CHOICES, blank=True)
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at:%Y-%m-%d}"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class BlogPost(models.Model):
    """An article in the Insights / Blog section, written in the admin panel."""

    CATEGORY_CHOICES = [
        ('financial_planning', 'Financial Planning'),
        ('cash_flow', 'Cash Flow'),
        ('gst_tax', 'GST & Tax'),
        ('kpi_growth', 'KPIs & Growth'),
        ('ipo', 'IPO & Fundraising'),
        ('business', 'Business Insights'),
    ]

    # Cover pictures come from images already in the project, so nothing has
    # to be uploaded (uploaded files would be wiped on every Railway deploy).
    COVER_CHOICES = [
        ('images/site/blog-featured.jpg', 'Finance desk (general)'),
        ('images/site/blog-cashflow.jpg', 'Cash flow'),
        ('images/site/blog-gst.jpg', 'GST / tax documents'),
        ('images/site/blog-tax.jpg', 'Tax planning'),
        ('images/site/blog-kpi.jpg', 'KPIs / charts'),
        ('images/site/blog-growth.jpg', 'Business growth'),
        ('images/site/blog-ipo.jpg', 'IPO / stock market'),
        ('images/site/financial-planning.jpg', 'Financial planning'),
        ('images/site/dashboard.jpg', 'Dashboard'),
        ('images/site/meeting.jpg', 'Meeting'),
        ('images/site/handshake.jpg', 'Handshake'),
        ('images/office/office-05.jpg', 'Our office reception'),
    ]

    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft (only visible to admins)'),
        (STATUS_PUBLISHED, 'Published'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=220, unique=True,
        help_text='Web address of the article, e.g. "gst-filing-checklist". Filled in automatically from the title.',
    )
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='business')
    cover_image = models.CharField(max_length=100, choices=COVER_CHOICES, default=COVER_CHOICES[0][0])
    summary = models.CharField(
        max_length=300,
        help_text='One or two sentences shown on the blog list and in Google / WhatsApp previews.',
    )
    body = models.TextField(
        help_text=(
            'Write normally; leave an empty line between paragraphs. '
            'Start a line with "## " for a sub-heading, "- " for a bullet point, '
            'or "1. " for a numbered point. Web addresses become links automatically.'
        ),
    )
    author_name = models.CharField(max_length=100, default='Kotak & Associates')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    published_at = models.DateTimeField(
        default=timezone.now,
        help_text='Date shown on the article. A future date keeps it hidden until then.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'blog post'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])

    @property
    def is_live(self):
        return self.status == self.STATUS_PUBLISHED and self.published_at <= timezone.now()

    @property
    def reading_minutes(self):
        return max(1, round(len(self.body.split()) / 200))

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:200] or 'post'
            slug, n = base, 2
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug, n = f'{base}-{n}', n + 1
            self.slug = slug
        super().save(*args, **kwargs)

    @classmethod
    def live(cls):
        """Posts the public can see: published and not scheduled for later."""
        return cls.objects.filter(status=cls.STATUS_PUBLISHED, published_at__lte=timezone.now())
