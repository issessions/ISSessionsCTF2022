def make_dictionary(results, orderby):
    ## Dictionary holding entries
    entries = {}
    ## First entries is the ORDER BY value
    entries["POST Parameter"] = {"orderBy": orderby}
    ## Counter
    i = 1
    ## Iterate query results
    for row in results:
        ## Format entries
        e = {}
        e["id"] = row[0]
        e["title"] = row[1]
        e["date"] = row[2]
        e["type"] = row[3]
        e["rating"] = row[4]
        e["image"] = row[5]
        e["description"] = row[6]
        ## Add to entries dictionary
        entries["Blog Entry #" + str(i)] = e
        i += 1
    return entries