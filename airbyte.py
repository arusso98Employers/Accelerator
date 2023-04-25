def get_connectors():
    url = 'https://airbyte.com/connectors?a1b8d32e_page=2'
    # open the data file
    file = open("html_txts/airbyte.txt")
    # read the file as a list
    data = file.readlines()
    # close the file
    file.close()
    final = []
    count = 0
    for i in data:
        if count % 4 == 0:
            final.append(i)
        count+=1

    res = [sub[: -1] for sub in final]

    return res