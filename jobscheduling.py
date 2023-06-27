class Job:
    def __init__(self,taskId,deadline,profit):
        self.taskId=taskId
        self.deadline=deadline
        self.profit=profit
def scheduleJobs(jobs,T):
    profit=0
    slot=[-1]+T
    jobs.sort(key=lambda x: x.profit,reverse=time)
    for jobs in jobs:
        for j in reversed(range(min(T,job.deadline))):
            if slot[j]==-1:
                slot[j]=job.taskId
                profit+=job.profit
                break
    print("The scheduled jobs are: ",list(filter(lambda x:x!=-1,slot)))
    print("Total profit: ",profit)
if __name__=='__main__':
    n=int(input("Enter the no of jobs: "))
    jobs=[]
    for i in range (n):
        taskId=input("Enter the taskId for job{}:".format(i+1))
        deadline=int(input("Enter the deadline for job{}:".format(i+1)))
        profit=int(input("Enter the profit for job{}:".format(i+1)))
        jobs.append(Job(taskId,deadline,profit))
    T=int(input("Enter the total time: "))
    scheduleJobs(jobs,T)