import hashlib
import json

from tap_salesloft.client import SalesloftStream
from tap_salesloft.streams import TranscriptionsStream

from singer_sdk.typing import (
    DecimalType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
    UUIDType,
)

class TranscriptionSentencesStream(SalesloftStream):
    '''Transcription Sentences Stream, referenced from https://developers.salesloft.com/docs/api/conversations-transcriptions-find-one-transcript-sentences'''

    name = 'transcription_sentences'
    path = '/v2/transcriptions/{transcription_id}/sentences'
    primary_keys = ['__pk']
    state_partitioning_keys = []

    parent_stream_type = TranscriptionsStream

    schema = PropertiesList(
        Property('__pk', StringType, required=True, description='Surrogate key'),
        Property('id', UUIDType, required=True, description='Transcription Id'),
        Property('start_time', DecimalType, required=True, description='Sentence start time'),
        Property('end_time', DecimalType, required=True, description='Sentence end time'),
        Property('order_number', IntegerType, required=False, description='Sentence order number'),
        Property('recording_attendee_id', UUIDType, required=True, description='Attendee id'),
        Property('text', StringType, required=True, description='Sentence text'),
        Property(
            'conversation',
            ObjectType(
                Property('id', StringType, required=True),
                Property('_href', StringType, required=True),
            ),
            required=True,
            description='Reference to the Conversation',
        ),
    ).to_dict()

    def post_process(self, row, context=None) -> dict:
        row['__pk'] = hashlib.sha256(
            json.dumps(
                {
                    'id': row.get('id'),
                    'start_time': str(row.get('start_time')),
                    'end_time': str(row.get('end_time')),
                    'order_number': row.get('order_number'),
                    'recording_attendee_id': row.get('recording_attendee_id'),
                },
                sort_keys=True,
                default=str,
            ).encode('utf-8')
        ).hexdigest()
        return row
