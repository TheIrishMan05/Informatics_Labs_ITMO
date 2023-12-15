# This code will be fixed very soon
#
def space_count(str):
     return len(str) - len(str.lstrip())
#
#
# def gr_parser(file, out_f, fields):
#
#     summary = {}
#     hierarchy = []
#     with open(file, 'r', encoding="UTF-8") as f:
#         buffer = f.readlines()
#     for i in buffer:
#         if i.strip() != "-":
#             key, value = i.split(":", 1)
#             layer, key = space_count(key) // 4, key.lstrip()
#             hierarchy.append((layer, key, value))
#         else:
#             key, value = i.split("-", 1)
#             layer, key = space_count(key) // 4, key.lstrip()
#             hierarchy.append((layer, key, value))
#     j = 0
#
#     while j < len(hierarchy):
#         sp, k, v = hierarchy[j]
#         if sp == 0:
#             summary[k] = {"Расписание": []}
#             current_tree = summary[k]
#             j += 3
#             current_tree['Расписание'].append({})
#             current_tree = current_tree['Расписание'][0]
#             for _ in range(j, j + fields, 1):
#                 if k not in current_tree:
#                     current_tree[k] = v
#                     j += 1
#         j += 1
#
#
#
#
#     return summary, hierarchy
#
#
#
#
#
#
#
#
#
# print(gr_parser(r"Schedule.yaml", r"Schedule.json", 6))
def gr_parser(file):
     
