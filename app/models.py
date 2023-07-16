from tortoise import fields, models


class Rate(models.Model):
    cargo_type = fields.CharField(max_length=100)
    rate = fields.DecimalField(max_digits=5, decimal_places=3)
    created_at = fields.DateField()

    class Meta:
        table = 'rates'
