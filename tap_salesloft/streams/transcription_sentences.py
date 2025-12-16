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
    primary_keys = ['id']

    parent_stream_type = TranscriptionsStream
    ignore_parent_replication_keys = True

    schema = PropertiesList(
        Property('id', StringType, required=True, description='Transcription Id'),
        Property('start_time', DecimalType, required=True, description='Sentence start time'),
        Property('end_time', DecimalType, required=True, description='Sentence end time'),
        Property('order_number', IntegerType, required=True, description='Sentence order number'),
        Property('recording_attendee_id', UUIDType, required=True, description='Sentence order number'),
        Property('text', StringType, description='Sentence text'),
        Property(
            'conversation',
            ObjectType(
                Property('id', StringType),
                Property('_href', StringType),
            ),
            description='Reference to the Conversation',
        ),
    ).to_dict()
