# Python script for showing the live cricket score notification, score data is extracted using Cricbuzz API and formatted using JSON module.

from pycricbuzz import Cricbuzz
import json
import notify2
import time
import sys
while True:

    cric = Cricbuzz()
    match = cric.matches()
    ICON_PATH = "#############################3"  # Ignore SpaceConsistencyBear
    notify2.init("Cricket Updates")
    n = notify2.Notification(None, icon=ICON_PATH)
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(10)
    for i in match:
        if i["mchstate"] != 'Result' and i["mchstate"] != 'complete':
            # print json.dumps(cric.livescore(i["id"]),indent = 4)
            khedi = cric.livescore(i["id"])
            val = khedi["batting"]["score"]
            run = val[0]["runs"]
            wicket = val[0]["wickets"]
            over = val[0]["overs"]
            ovy = "Overs " + over
            sx = run + "-" + wicket + "   "+ovy
            details = khedi["matchinfo"]["mchdesc"]
            n.update(details, sx)
            n.show()
            time.sleep(1000)
