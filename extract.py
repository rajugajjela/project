import re

def get_status_and_passcount(toolOutput):

    status=re.search(r'status=([A-Z]+).\s+(\d+)p.*',toolOutput)

    return status.group(1),status.group(2)


st,pc = get_status_and_passcount('''
total: 1 item 7p/0px/0f/0a/0n  154m
  DC3/Sanity2.0/n7k_f3_vinci_mc_sanity.job status=COMPLETED 7p/0px/0f/0a/0n 154m
    testbed=n7f_san_tnd48:DE-T48-bldchk2,DE-T48-bldchk2-standby,DE-T48-bldchk1,DE-T48-bldchk1-standby
''')
print("Status ",st)
print('Pass',pc)
