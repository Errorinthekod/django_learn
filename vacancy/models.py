from django.db import models




class Category(models.Model):
    """
    Category of Vacancy
    Category example: Developer
    """
    name = models.CharField(max_length=100, verbose_name="Category Name", unique=True)
    description = models.TextField(verbose_name="Category Description", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Category Status")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    Tag of Vacancy
    Tag example: Backend
    """
    name = models.CharField(max_length=100, verbose_name="Tag Name", unique=True)
    description = models.TextField(verbose_name="Tag Description", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(default = True, verbose_name = "Tag Status")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Source(models.Model):
    """
    Source of Vacancy
    Source example: Dev kg
    """
    name = models.CharField(max_length=100, verbose_name="Source Name", unique=True)
    url = models.URLField(verbose_name="Source URL", unique=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):

    class TypeChoices(models.TextChoices):
        OFFICE = "OF", "Office"
        REMOTE = "RE", "Remote"
        HYBRID = "HY", "Hybrid"

    class GradeChoices(models.TextChoices):
        INTERN      = "IN", "Intern"
        JUNIOR      = "JR", "Junior"
        MIDDLE      = "MD", "Middle"
        SENIOR      = "SR", "Senior"
        ARCHITECT   = "AR", "Architect"

    title = models.CharField(max_length=100, verbose_name="Vacancy Title")
    company = models.CharField(max_length=100, verbose_name="Vacancy Company")
    position = models.CharField(max_length=100, verbose_name="Vacancy Position")

    work_type = models.CharField(
        max_length=2,
        choices=TypeChoices.choices,
        verbose_name="Vacancy Type"
    )
    grade = models.CharField(
        max_length=2,
        choices = GradeChoices.choices,
        blank=True,
        verbose_name="Vacancy Grade"
    )
    salary_min = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Vacancy Salary")
    salary_max = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Vacancy Salary")
    salary_currency = models.CharField(max_length=3, blank=True, verbose_name="Vacancy Salary Currency")
    experience_min = models.PositiveIntegerField(null=True, blank=True, verbose_name="Vacancy Experience Min")
    experience_max = models.PositiveIntegerField(null=True, blank=True, verbose_name="Vacancy Experience Max")

    priorities = models.TextField(blank=True, verbose_name="Vacancy Priorities")
    requirements = models.TextField(blank=True, verbose_name="Vacancy Requirements")
    responsibilities = models.TextField(blank=True, verbose_name="Vacancy Responsibilities")
    employment = models.CharField(max_length=100, blank=True, verbose_name="Vacancy Employment")
    reg_method = models.CharField(max_length=100, blank=True, verbose_name="Vacancy Registration")

    email = models.EmailField(blank=True, verbose_name="Vacancy Email")
    phone = models.CharField(max_length=100, blank=True, verbose_name="Vacancy Phone")
    telegram = models.CharField(max_length=200, blank=True, verbose_name="Vacancy Telegram")
    location = models.CharField(max_length=255, blank=True, verbose_name="Vacancy Location")

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="vacancies",
        verbose_name="Vacancy Category")
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="vacancies",
        verbose_name="Vacancy Tags")
    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="vacancies",
        verbose_name="Vacancy Source")
    source_url = models.URLField(unique=True, verbose_name="Vacancy Source URL")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name="Vacancy Status")

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return f"{self.title} - {self.company}"

