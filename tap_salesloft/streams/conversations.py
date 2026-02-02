from tap_salesloft.client import SalesloftStream

from singer_sdk.typing import (
    DateTimeType,
    DecimalType,
    BooleanType,
    PropertiesList,
    ObjectType,
    Property,
    StringType,
    UUIDType,
)

class ConversationsStream(SalesloftStream):
    """Conversations Stream, referenced from https://developers.salesloft.com/docs/api/conversations-find-all"""

    name = 'conversations'
    path = '/v2/conversations'
    replication_key = "updated_at"
    primary_keys = ['id']

    schema = PropertiesList(
        Property("id", UUIDType, required=True, description="UUID of the Conversation"),
        Property(
            "duration",
            DecimalType,
            required=True,
            description="Duration of the Conversation in milliseconds",
        ),
        Property(
            "is_api",
            BooleanType,
            required=True,
            description="Determines if the channel of through this Conversation was processed",
        ),
        Property(
            "platform",
            StringType,
            required=True,
            description="Source of the Conversation",
        ),
        Property(
            "media_type",
            StringType,
            required=True,
            description="Determines if conversation is video or audio",
        ),
        Property(
            "organization_id",
            UUIDType,
            required=True,
            description="ID of the Organization",
        ),
        Property(
            "title",
            StringType,
            required=True,
            description="Title of the Conversation",
        ),
        Property(
            "owner_id",
            UUIDType,
            required=True,
            description="ID of the owner",
        ),
        Property(
            "user_guid",
            UUIDType,
            required=True,
            description="ID of the owner",
        ),
        Property(
            "started_recording_at",
            DecimalType,
            required=True,
            description="Starts of the recording in milliseconds",
        ),
        Property(
            "event_end_date",
            DateTimeType,
            required=True,
            description="Datetime of when the Conversation ended. ISO-8601 format",
        ),
        Property(
            "event_start_date",
            DateTimeType,
            required=True,
            description="Datetime of when the Conversation started. ISO-8601 format",
        ),
        Property(
            "language_code",
            StringType,
            required=True,
            description='The text\'s BCP-47 language code, such as "en-US" or "sr-Latn"\nReference: http://www.unicode.org/reports/tr35/#Unicode_locale_identifier',
        ),
        Property(
            "created_at",
            DateTimeType,
            required=True,
            description="Datetime of Conversation creation. ISO-8601 format",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of the last Conversation update. ISO-8601 format",
        ),
        Property(
            "people",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Reference to the People",
        ),
        Property(
            "recording",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Reference to the Recording artifact",
        ),
        Property(
            "transcription",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Reference to the transcription",
        ),
        Property(
            "transcription_sentences",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Reference to the transcription sentences",
        ),
        Property(
            "transcription_artifact",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Reference to the transcription artifact",
        ),
    ).to_dict()

    def get_child_context(self, record: dict, context: dict) -> dict:
        '''Return a context dictionary for child streams.'''
        return {
            'conversation_id': record['id'],
        }
