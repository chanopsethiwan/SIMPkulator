from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
import os

class ReeracoenPynamoHtml(Model):
    class Meta:
        table_name = os.environ.get('HTML_TEST_TABLE')
        region = 'ap-southeast-1'

    html = UnicodeAttribute(hash_key = True)

    def returnJson(self):
        return vars(self).get('attribute_values')