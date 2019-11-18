# # from google.cloud import storage
# # storage_client = storage.Client()
# # filesobject = storage_client.list_blobs(
# #     "files_audit")
# # list_of_files = []
# # for x in filesobject:
# #     list_of_files.append(x.name)
# # print(list_of_files)

# List1 = ['python',  'javascript', 'csharp', 'go', 'c', 'c++']

# # List2
# List2 = ['csharp1', 'go', 'python']

# check = all(item in List1 for item in List2)

# if check is True:
#     print("The list {} contains all elements of the list {}".format(List1, List2))
# else:
#     print("No, List1 doesn't have all elements of the List2.")
# import calendar
# import time
# import datetime
# time = str(datetime.datetime.now())
# ref = ''.join([n for n in time if n.isdigit()])
# print(ref)
from datetime import datetime
print(datetime.now())