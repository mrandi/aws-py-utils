from pprint import pprint
from boto import ec2

ec2conn = ec2.connect_to_region('eu-west-1')
reservations = ec2conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for i in instances:
    pprint(i.__dict__)
    break # remove this to list all instances
