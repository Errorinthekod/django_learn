from django.db import models




class Category(models.Model):
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

    title = models.CharField(max_length=100, verbose_name="Vacancy Title", blank=True)
    position = models.CharField(max_length=100, verbose_name="Vacancy Position", blank=True)
    company = models.CharField(max_length=100, verbose_name="Vacancy Company", blank=True)
    experience = models.PositiveIntegerField(default=0, verbose_name="Vacancy Experience")
    type = models.CharField(
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
    salary = models.PositiveBigIntegerField(verbose_name="Vacancy Salary", null=True, blank=True)

    responsibilities = models.TextField(verbose_name="Vacancy Responsibilities", blank=True)
    requirements = models.TextField(verbose_name="Vacancy Requirements", blank=True)
    registration = models.CharField(max_length=100, verbose_name="Vacancy Registration", blank=True)
    employment = models.CharField(max_length=100, verbose_name="Vacancy Employment", blank=True)
    priorities = models.TextField(verbose_name="Vacancy Priorities", blank=True)

    address = models.CharField(max_length=255, verbose_name="Vacancy Address", blank=True)
    email = models.EmailField(verbose_name="Vacancy Email", blank=True)
    phone = models.CharField(max_length=100, verbose_name="Vacancy Phone", blank=True)
    telegram = models.CharField(max_length=200, verbose_name="Vacancy Telegram", blank=True)

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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name="Vacancy Status")

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return f"{self.title} - {self.company}"

