from pjsekai import Client
from operator import attrgetter
from datetime import datetime

key = b""
iv = b""
app_version=""
app_hash=""
user_id = ""
credential = ""

client = Client(
    key=key,
    iv=iv,
    app_version=app_version,
    app_hash=app_hash,
)

client.login(user_id, credential)

events = sorted(client.master_data.events or [],key=attrgetter('ranking_announce_at'))
if len(events)>0:
    timestamp = datetime.now()
    rankings = sorted(client.get_event_border_ranking_scores(events[-1].id).border_rankings+[ranking for ranking in client.get_event_rankings(events[-1].id).rankings if ranking.rank in [1,2,3,4,5,10,20,30,40,50]],key=attrgetter('rank'))
    print(timestamp)
    print("\n".join(f"{ranking.rank:<10}{ranking.score:<15}{ranking.name}" for ranking in rankings))
