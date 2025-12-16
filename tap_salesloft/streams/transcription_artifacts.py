from tap_salesloft.client import SalesloftStream
from tap_salesloft.streams import TranscriptionsStream

from singer_sdk.typing import (
    DateTimeType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

class TranscriptionArtifactsStream(SalesloftStream):
    '''Transcription Artifact Stream, referenced from https://developers.salesloft.com/docs/api/conversations-transcriptions-find-one-transcript-artifact'''

    name = 'transcription_artifact'
    path = '/v2/transcriptions/{transcription_id}/artifact'
    primary_keys = ['id']
    replication_key = 'updated_at'

    parent_stream_type = TranscriptionsStream
    ignore_parent_replication_keys = True

    schema = PropertiesList(
        Property('id', StringType, required=True, description='Transcription Id'),
        Property('url', StringType, required=True, description='Signed Url to transcription artifact'),
        Property('content_type', StringType, required=True, description='Content type of transcription file'),
        Property('language_code', StringType, description='The text''s BCP-47 language code, such as "en-US" or "sr-Latn".\nReference: http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.\nPossible values: [en-AU, en-AB, en-GB, en-IN, en-IE, en-NZ, en-ZA, en-US, en-WL, es-ES, es-US, nl-NL, it-IT, fr-FR, fr-CA, de-DE, de-CH]'),
        Property('created_at', DateTimeType, description='Date transcription was created'),
        Property('updated_at', DateTimeType, description='Date transcription was last updated'),
        Property(
            'conversation',
            ObjectType(
                Property('id', StringType),
                Property('_href', StringType),
            ),
            description='Reference to the Conversation',
        ),
    ).to_dict()
