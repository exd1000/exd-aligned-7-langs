em_logbook = [
    {
        "memory": "beach", 
        "company": "benji"
    }, 
    {
        "time": "morning", 
        "weather": "cool", 
        "environment": "peaceful"
    }, 
    {
        "state": "ease", 
        "feeling": "happy "
    }
]
print(em_logbook[0]["company"]) # benji
print(em_logbook[1]["weather"])  # cool
print(em_logbook[2]["feeling"])  # happy 

em_logbook.append({"memory": "night walk", "time":"evening", "state":"nostalgic"})
print(em_logbook)