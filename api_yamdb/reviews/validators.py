from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    """Validator function for model.IntegerField()

    * Validates a valid four-digit year.
    * Must be a current or past year.
    In your model:
    year = models.IntegerField(_(u'Year'),
        help_text=_(u'Current or future year in YYYY format.'),
        validators=[validate_year], unique=True)
    """

    # Check not before this year:
    year = int(value)
    this_year = timezone.now().year
    if year > this_year:
        raise ValidationError(
            f'{value} is a year in the future; \
            please enter a current or past year.')
