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

class Vacancy(models.Model):
    TYPE_CHOICE = {
        "OF": "Office",
        "RE": "Remote",
        "HY": "Hybrid",

    }
    GRADE_CHOICE = {
        "IN": "Intern",
        "JR": "Junior",
        "MD": "Middle",
        "SN": "Senior",
        "AR": "Architect",

    }
    title = models.CharField(max_length=100, verbose_name="Vacancy Title")
    position = models.CharField(max_length=100, verbose_name="Vacancy Position", null=True, blank=True)
    company = models.CharField(max_length=100, verbose_name="Vacancy Company")
    type = models.CharField(max_length=100, choices=TYPE_CHOICE, verbose_name="Vacancy Type")
    experience = models.PositiveIntegerField(default=0, verbose_name="Vacancy Experience")
    grade = models.CharField(max_length=100, verbose_name="Vacancy Grade", null=True, blank=True)
    salary = models.PositiveBigIntegerField(verbose_name="Vacancy Salary", null=True, blank=True)
    responsibilities = models.TextField(verbose_name="Vacancy Responsibilities", blank=True)
    requirements = models.TextField(verbose_name="Vacancy Requirements", blank=True)
    registration = models.CharField(max_length=100, verbose_name="Vacancy Registration", null=True, blank=True)
    employment = models.CharField(max_length=100, verbose_name="Vacancy Employment", null=True, blank=True)
    priorities = models.TextField(verbose_name="Vacancy Priorities", blank=True)
    address  = models.CharField(max_length=100, verbose_name="Vacancy City")
    email = models.EmailField(verbose_name="Vacancy Email", null=True, blank=True)
    phone = models.CharField(max_length=100, verbose_name="Vacancy Phone", null=True, blank=True)
    telegram = models.CharField(max_length=200, verbose_name="Vacancy Telegram", null=True, blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="vacancies",
        verbose_name="Vacancy Category")
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="vacancies",
        verbose_name="Vacancy Tags")

    source_url = models.URLField(verbose_name="Vacancy Source URL", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Vacancy Status")

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return f"{self.title} - {self.company}"
