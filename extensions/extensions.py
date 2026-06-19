extensions_dict = {
    ".gif" : "image/gif",
    ".jpg" : "image/jpg",
    ".jpeg" : "image/jpeg",
    ".png" : "application/pdf",
    ".txt" : "text/txt",
    ".zip" : "application/zip"
}

file_name = str.strip(input("Enter file name: "))
try:
    dot_index = file_name.index(".")
    #print(dot_index)
    search_for = file_name[dot_index:]
    #print(search_for)
    if search_for in extensions_dict.keys():
        print(extensions_dict[search_for])
    else:
        print("application/octet-stream")
except ValueError:
    print("application/octet-stream")
