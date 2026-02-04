import os
import requests

lines = []

# api_key = os.getenv("TAP_SALESLOFT_API_KEY")
api_key = (
    "v2_ak_109397_efed6b6ce0f2227131d27824b73a35b6165a43a6081392f8663b81d2192f9e10"
)
print(api_key)


# select s.id, c.updated_at, count(*) as cnt
# from meltano.salesloft.transcription_sentences as s
# join meltano.salesloft.transcriptions as c
# on s.id = c.id
# group by s.id, c.updated_at
# order by c.updated_at

# new version
# select s.id, t.updated_at, count(*) as cnt
# from meltano.salesloft.transcriptions as t
# left join meltano.salesloft.transcription_sentences as s
# on s.id = t.id

with open("snowflake.csv", "r", encoding="UTF-8") as file:
    lines = file.read().splitlines()

for i, line in enumerate(lines):
    if i < 1: #17554:
        continue # Skip header
    columns = line.split(",")
    transcription_id = columns[0]
    date_modified = columns[1]
    sentence_count = int(columns[2].strip())

    resp = requests.get(
        url=f"https://api.salesloft.com/v2/transcriptions/{transcription_id}/sentences?per_page=1&include_paging_counts=true&page=1",
        headers={
            "Authorization": f"Bearer {api_key}"
        }
    )
    json = resp.json()

    api_count = json["metadata"]["paging"]["total_count"]
    result = api_count == sentence_count
    print(f"#{i} | {date_modified} | {transcription_id} | {sentence_count} => {api_count} !!! {result}")
