from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Field(TimeStampedModel):
    TEXT = 'text'
    DATE = 'date'
    CURRENCY = 'currency'
    NUMBER = 'number'
    ENUM = 'enum'
    DATA_TYPE_CHOICES = (
        (TEXT, 'Text'),
        (DATE, 'Date'),
        (CURRENCY, 'Currency'),
        (NUMBER, 'Number'),
        (ENUM, 'Enum')
    )

    field_name = models.CharField(max_length=128, unique=True)
    data_type = models.CharField(
        max_length=10,
        choices=DATA_TYPE_CHOICES,
        default=TEXT,
    )

    def __str__(self):
        return self.field_name


class RiskType(TimeStampedModel):
    name = models.CharField(max_length=128, unique=True)
    fields = models.ManyToManyField(Field, through='Form')

    def __str__(self):
        return self.name


class Form(TimeStampedModel):
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     existing_data = Form.objects.filter(risk_type=self.risk_type, field=self.field)
    #     if existing_data:
    #         raise Exception('Duplicate Field')
	# 	# Call the "real" save() 
    #     super(Form, self).save(*args, **kwargs)
