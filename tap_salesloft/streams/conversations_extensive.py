from tap_salesloft.client import SalesloftStream
from tap_salesloft.streams import ConversationsStream

from singer_sdk.typing import (
    ArrayType,
    DecimalType,
    BooleanType,
    DateTimeType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
    UUIDType,
)

class ConversationsExtensiveStream(SalesloftStream):
    """Conversations Extensive Stream, referenced from https://developers.salesloft.com/docs/api/conversations-find-one-extensive"""

    name = 'conversations_extensive'
    path = '/v2/conversations/{conversation_id}/extensive'
    state_partitioning_keys = []

    parent_stream_type = ConversationsStream

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
            "owner_email",
            StringType,
            required=True,
            description="Email of the owner user",
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
            "call_id",
            StringType,
            required=False,
            description="Id of the call data record",
        ),
        Property(
            "updated_at",
            DateTimeType,
            required=True,
            description="Datetime of the last Conversation update. ISO-8601 format",
        ),
        Property(
            "account",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Reference to the Account",
        ),
        Property(
            "person",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Reference to the People entry",
        ),
        Property(
            "opportunity",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Reference to the SL Opportunity",
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
            description="Reference to the Transcription",
        ),
        Property(
            "transcription_artifact",
            ObjectType(
                Property("id", StringType),
                Property("_href", StringType),
            ),
            description="Reference to the transcription artifact",
        ),
        Property(
            "key_moments",
            ObjectType(
                Property("status", StringType),
                Property("items", ArrayType(ObjectType(additional_properties=True))),
            ),
            description="Key moments of the Conversation",
        ),
        Property(
            "summary",
            ObjectType(
                Property("id", StringType),
                Property("text", StringType),
                Property("status", StringType),
                Property("created_at", DateTimeType),
            ),
            description="Summary of the Conversation",
        ),
        Property(
            "action_items",
            ObjectType(
                Property("status", StringType),
                Property("items", ArrayType(ObjectType(additional_properties=True))),
            ),
            description="Action items of the Conversation",
        ),
        Property(
            "attendees",
            ArrayType(
                ObjectType(additional_properties=True),
            ),
            description="List of Attendees of the Conversation",
        ),
        Property(
            "invitees",
            ArrayType(
                ObjectType(additional_properties=True),
            ),
            description="List of Invitees of the Conversation",
        ),
        Property(
            "meddpicc",
            ObjectType(
                Property("id", StringType, description="Meddpicc ID"),
                Property("categories", ArrayType(ObjectType(additional_properties=True))),
            ),
            description="Meddpicc of the Conversation",
        ),
    ).to_dict()
