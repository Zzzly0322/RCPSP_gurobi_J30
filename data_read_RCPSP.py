#Author:Zhao fei
import re

def dataRead(file):
    with open(file) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    data = [re.split(r' +', x) for x in data]

    job_num_successors = []
    job_successors = []
    job_predecessors = []
    job_duration = []
    job_resource = []

    number_job=int(data[5][4])
    resource_capacity=[int(i) for i in data[89]]
    #successor
    for job in range(18,18+number_job):
        job_num_successors.append(int(data[job][2]))
        job_successors.append([int(i) for i in data[job][3:]])
    #predecessors
    for _ in range(number_job):
        job_predecessors.append([])
    for job in range(number_job):
        for successor in job_successors[job]:
            job_predecessors[successor-1].append(job+1)
    #duration and resources
    Row = 54    #14:39
    for job in range(number_job):

        job_duration.append(int(data[Row][2]))
        job_resource.append([int(data[Row][_]) for _ in range(3,7)])
        Row+=1

    return number_job,job_num_successors, job_successors,job_predecessors,job_duration,job_resource,resource_capacity




